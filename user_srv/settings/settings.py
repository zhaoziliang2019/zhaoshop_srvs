import json

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
    "NameSpace": "c0c8e1ce-b20c-4676-9a63-079b6d8d75b5",
    "User": "nacos",
    "Password": "nacos",
    "DataId": "user-srv.json",
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

# 服务相关的配置
SERVICE_NAME = data["name"]
SERVICE_TAGS = data["tags"]
