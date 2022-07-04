import json

import redis
from loguru import logger
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

import nacos


# 使用peewee的连接池，使用ReconnectMixin来防止出现连接断开查询失败
# mysql gone away


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


NACOS = {
    "Host": "192.168.1.31",
    "Port": 8848,
    "NameSpace": "0277fead-c0de-4562-8abf-62918f18af67",
    "User": "nacos",
    "Password": "nacos",
    "DataId": "inventory-srv.json",
    "Group": "dev",
}
client = nacos.NacosClient(
    f'{NACOS["Host"]}:{NACOS["Port"]}', namespace=NACOS["NameSpace"]
)
# get config
data = client.get_config(NACOS["DataId"], NACOS["Group"])
data = json.loads(data)
logger.info(data)


# update config
def update_config(args):
    logger.info("config 发生变化")
    logger.info(args)


# MYSQL_DB="zhaoshop_user_srv"
# MYSQL_HOST="192.168.1.26"
# MYSQL_PORT=3306
# MYSQL_USER="root"
# MYSQL_PASSWORD="root"
DB = ReconnectMysqlDatabase(
    data["mysql"]["db"],
    host=data["mysql"]["host"],
    port=data["mysql"]["port"],
    user=data["mysql"]["user"],
    password=data["mysql"]["password"],
)

# consul的配置
CONSUL_HOST = data["consul"]["host"]
CONSUL_PORT = data["consul"]["port"]
# rocketmq的配置
ROCKETMQ_HOST = data["rocketmq"]["host"]
ROCKETMQ_PORT = data["rocketmq"]["port"]
# 服务相关的配置
SERVICE_NAME = data["name"]
SERVICE_TAGS = data["tags"]

REDIS_HOST = data["redis"]["host"]
REDIS_PORT = data["redis"]["port"]
REDIS_DB = data["redis"]["db"]
# 配置一个连接池
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
REDIS_CLIENT = redis.StrictRedis(connection_pool=pool)
