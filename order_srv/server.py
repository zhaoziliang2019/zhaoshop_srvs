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
from jaeger_client import Config
from loguru import logger
from rocketmq.client import PushConsumer

from common.grpc_health.v1 import health_pb2_grpc, health
from common.register import consul
from grpc_opentracing import open_tracing_server_interceptor
from grpc_opentracing.grpcext import intercept_server
from order_srv.handler.order import OrderServicer, order_timeout
from proto import order_pb2_grpc
from settings import settings

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
    # jaeger
    config = Config(
        config={  # usually read from some yaml config
            "sampler": {
                "type": "const",
                "param": 1,
            },
            "local_agent": {
                "reporting_host": "192.168.1.31",
                "reporting_port": "6831",
            },
            "logging": True,
        },
        service_name="order-srv",
        validate=True,
    )
    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip", nargs="?", type=str, default="192.168.1.16", help="binding ip"
    )
    parser.add_argument(
        "--port", nargs="?", type=int, default=0, help="the listening port"
    )
    args = parser.parse_args()
    # 动态分配ip
    args.ip = get_free_tcp_ip()
    # 动态分配port
    if args.port == 0:
        port = get_free_tcp_port()
    else:
        port = args.port

    logger.add("logs/order_srv_{time}.log")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # jaeger
    tracing_interceptor = open_tracing_server_interceptor(tracer)
    server = intercept_server(server, tracing_interceptor)
    # 注册库存服务
    order_pb2_grpc.add_OrderServicer_to_server(OrderServicer(), server)
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
    # 监听超时订单消息
    consumer = PushConsumer("zhaoshop_order")
    consumer.set_name_server_address(
        f"{settings.ROCKETMQ_HOST}:{settings.ROCKETMQ_PORT}"
    )
    consumer.subscribe("order_timeout", order_timeout)
    consumer.start()
    server.wait_for_termination()
    consumer.shutdown()


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
