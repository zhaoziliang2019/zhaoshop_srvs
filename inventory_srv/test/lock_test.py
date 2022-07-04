import time
from datetime import datetime

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


import threading

R = threading.Lock()


def sell():
    goods_list = [(421, 99), (422, 20), (423, 30)]
    with settings.DB.atomic() as txn:
        for goods_id, num in goods_list:
            # 查询库存
            R.acquire()
            goods_inv = Inventory.get(Inventory.goods == goods_id)
            from random import randint

            time.sleep(randint(1, 3))
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
            R.release()


def sell2():
    # 演示mysql分布式锁
    goods_list = [(421, 10), (422, 20), (423, 30)]
    with settings.DB.atomic() as txn:
        for goods_id, num in goods_list:
            # 查询库存
            while True:
                goods_inv = Inventory.get(Inventory.goods == goods_id)
                from random import randint

                time.sleep(randint(1, 3))
                if goods_inv.stocks < num:
                    print(f"商品：{goods_id}库存不足")
                    txn.rollback()
                    break
                else:
                    # 让数据库根据自己当前的值更新数据，这个语句不能处理并发的问题
                    # 我当时查询数据的时候版本号是goods_inv.version 乐观锁
                    query = Inventory.update(
                        stocks=Inventory.stocks - num, version=Inventory.version + 1
                    ).where(
                        Inventory.goods == goods_id,
                        Inventory.version == goods_inv.version,
                    )
                    ok = query.execute()
                    if ok:
                        print("更新成功")
                        break
                    else:
                        print("更新失败")
                    # goods_inv.stocks -= num
                    # goods_inv.save()


if __name__ == "__main__":
    import threading

    t1 = threading.Thread(target=sell2)
    t2 = threading.Thread(target=sell2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
