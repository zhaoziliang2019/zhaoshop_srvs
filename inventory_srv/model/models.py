from datetime import datetime

from peewee import *
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

from inventory_srv.settings import settings


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


# MYSQL_DB = "zhaoshop_goods_srv"
# MYSQL_HOST = "192.168.1.31"
# MYSQL_PORT = 3306
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "root"
# DB = ReconnectMysqlDatabase(
#     "zhaoshop_inventory_srv",
#     host=MYSQL_HOST,
#     port=MYSQL_PORT,
#     user=MYSQL_USER,
#     password=MYSQL_PASSWORD,
# )


# 删除-物理删除和逻辑删除
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


class InventoryHistory(BaseModel):
    # 出库历史表
    order_sn = CharField(verbose_name="订单编号", max_length=20, unique=True)
    order_inv_detail = CharField(verbose_name="订单详情", max_length=200)
    status = IntegerField(
        choices=((1, "已扣减"), (2, "已归还")), default=1, verbose_name="出库状态"
    )


if __name__ == "__main__":
    settings.DB.create_tables([Inventory, InventoryHistory])
    # for i in range(421, 841):
    #     try:
    #         inv = Inventory.get(Inventory.goods == i)
    #         inv.stocks = 100
    #         inv.save()
    #     except DoesNotExist as e:
    #         inv = Inventory(goods=i, stocks=100)
    #         inv.save(force_insert=True)
