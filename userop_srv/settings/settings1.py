from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

# 使用peewee的连接池，使用ReconnectMixin来防止出现连接断开查询失败
# mysql gone away


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


MYSQL_DB = "zhaoshop_user_srv"
MYSQL_HOST = "192.168.1.26"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
DB = ReconnectMysqlDatabase(
    "zhaoshop_user_srv",
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
)

# consul的配置
CONSUL_HOST = "192.168.1.26"
CONSUL_PORT = 8500

# 服务相关的配置
SERVICE_NAME = "user-srv"
SERVICE_TAGS = ["zhaoshop", "python", "srv"]
