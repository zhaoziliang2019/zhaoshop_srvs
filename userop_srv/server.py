# 启动grpc
import argparse
import logging
import os.path
import signal
import socket
import sys
from concurrent import futures
from functools import partial

import grpc
from loguru import logger

from common.grpc_health.v1 import health_pb2_grpc, health
from common.register import consul
from proto import message_pb2_grpc, address_pb2_grpc, userfav_pb2_grpc
from settings import settings
from userop_srv.handler.address import AddressServicer
from userop_srv.handler.message import MessageServicer
from userop_srv.handler.user_fav import UserFavServicer

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(BASE_DIR)
sys.path.insert(0, BASE_DIR)


# 退出服务
def on_exit(signo, frame, service_id):
    register = consul.ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    logger.info(f"注销{service_id} 服务")
    register.deregister(service_id == service_id)
    logger.info("注销成功")
    sys.exit(0)


# 自动获取端口
def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("", 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


# 自动获取本机ip
def get_free_tcp_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", nargs="?", type=str, default=0, help="binding ip")
    parser.add_argument(
        "--port", nargs="?", type=int, default=0, help="the listening port"
    )
    args = parser.parse_args()
    # 动态获取ip
    args.ip = get_free_tcp_ip()
    # 动态分配port
    if args.port == 0:
        port = get_free_tcp_port()
    else:
        port = args.port

    logger.add("logs/userop_srv_{time}.log")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册用户服务
    message_pb2_grpc.add_MessageServicer_to_server(MessageServicer, server)
    address_pb2_grpc.add_AddressServicer_to_server(AddressServicer, server)
    userfav_pb2_grpc.add_UserFavServicer_to_server(UserFavServicer, server)
    # 注册健康检查
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    server.add_insecure_port(f"{args.ip}:{port}")
    # 主进程退出信号监听
    """
    windows下支持的信号是有限的：
       SIGINT ctrl+c终端
       SIGTERM kill发出的软件终止
    """
    import uuid

    service_id = str(uuid.uuid1())

    signal.signal(signal.SIGINT, partial(on_exit, service_id=service_id))
    signal.signal(signal.SIGTERM, partial(on_exit, service_id=service_id))

    logger.info(f"启动服务：{args.ip}:{port}")
    server.start()

    # 注册consul
    logger.info(f"consul服务注册开始")
    register = consul.ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    if not register.register(
        name=settings.SERVICE_NAME,
        id=service_id,
        address=args.ip,
        port=port,
        tags=settings.SERVICE_TAGS,
        check=None,
    ):
        logger.error(f"consul服务注册失败")
        sys.exit(0)
    logger.info(f"consul服务注册成功")
    server.wait_for_termination()


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


if __name__ == "__main__":
    # print(get_free_tcp_port())
    logging.basicConfig()
    settings.client.add_config_watcher(
        settings.NACOS["DataId"], settings.NACOS["Group"], settings.update_config
    )
    serve()
