import threading
import time
import uuid
from datetime import datetime

import redis
from peewee import *
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

from inventory_srv.settings import settings


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now, verbose_name="添加时间")
    is_deleted = BooleanField(default=False, verbose_name="是否删除")
    update_time = DateTimeField(default=datetime.now, verbose_name="更新时间")

    @classmethod
    def delete(cls, permanently=False):  # permanently表示是否永久删除
        if permanently:
            return super().delete()
        else:
            return super().update(is_deleted=True)

    def delete_instance(
        self, permanently=False, recursive=False, delete_nullable=False
    ):
        if permanently:
            return self.delete(permanently).where(self._pk_expr()).execute()
        else:
            self.is_deleted = True
            self.save()

    @classmethod
    def select(cls, *fields):
        return super().select(*fields).where(cls.is_deleted == False)

    def save(self, *args, **kwargs):
        # 判断这是一个新添加的数据还是更新的数据
        if self._pk is not None:
            # 这是一个新数据
            self.update_time = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = settings.DB


class Inventory(BaseModel):
    # 商品的库存表
    goods = IntegerField(verbose_name="商品id", unique=True)
    stocks = IntegerField(verbose_name="库存数量", default=0)
    version = IntegerField(verbose_name="版本号", default=0)  # 分布式锁的乐观锁


class Lock:
    def __init__(self, name, id=None):
        self.id = uuid.uuid4()
        self.redis_client = redis.Redis(host="192.168.1.31", port=6379, db=0)
        self.name = name

    def acquire(self):
        if self.redis_client.set(self.name, self.id, nx=True, ex=15):
            # if self.redis_client.setnx(self.name, 1):  # 如果不存在设置并返回1，否则返回0，原子操作
            # if not self.redis_client.get(self.name):
            #     # 如果为空或者为None那么代表获取到锁
            #     self.redis_client.set(self.name, 1)
            #   启动一个线程然后去定时的刷新这个过期，这个操作最好也是使用lua脚本来完成
            return True
        else:
            while True:
                import time

                time.sleep(1)
                # if self.redis_client.get(self.name):
                # if self.redis_client.setnx(self.name, 1):
                if self.redis_client.set(self.name, self.id, nx=True, ex=15):
                    return True

    def release(self):
        # 先做一个判断，先取出来值然后判断当前的值和你自己的lock中的id是否一致，如果一致删除，如果不一致报错
        # 这块代码不安全，将get和delete操作原子化 -但是redis提供了一个脚本语言-lua-nigix
        # 使用lua脚本完成这个操作使得该操作原子化
        id = self.redis_client.get(self.name)
        if id == self.id:
            self.redis_client.delete(self.name)
        else:
            print("不能删除不属于自己的锁")


def sell():
    goods_list = [(421, 10), (422, 20), (423, 30)]
    with settings.DB.atomic() as txn:
        # 超卖
        # 续租过期时间-看门狗 -java中有一个redisson
        # 如何防止我设置的值被其他的线程给删除掉uuid
        for goods_id, num in goods_list:
            # 查询库存
            # lock = Lock(f"lock:goods_{goods_id}")
            # lock.acquire()
            # 第三方redis
            from inventory_srv.test.py_redis_lock import Lock as PyLock

            redis_client = redis.Redis(host="192.168.1.31")
            lock = PyLock(
                redis_client, f"lock:goods_{goods_id}", auto_renewal=True, expire=15
            )
            lock.acquire()
            goods_inv = Inventory.get(Inventory.goods == goods_id)

            time.sleep(20)
            if goods_inv.stocks < num:
                print(f"商品：{goods_id}库存不足")
                txn.rollback()
                break
            else:
                # 让数据库根据自己当前的值更新数据，这个语句不能处理并发的问题
                query = Inventory.update(stocks=Inventory.stocks - num).where(
                    Inventory.goods == goods_id
                )
                ok = query.execute()
                if ok:
                    print("更新成功")
                else:
                    print("更新失败")
                # goods_inv.stocks -= num
                # goods_inv.save()
            lock.release()


if __name__ == "__main__":
    # redis_client = redis.Redis(host="192.168.1.31", port=6379, db=0)
    # goods_id = 1
    # print(redis_client.get(f"lock:goods_{goods_id}"))
    t1 = threading.Thread(target=sell)
    t2 = threading.Thread(target=sell)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
