import time

from rocketmq.client import TransactionMQProducer, Message, TransactionStatus

topic = "TopicTest"


def create_message():
    msg = Message(topic)
    msg.set_keys("zhao")
    msg.set_tags("shop")
    msg.set_property("name", "services")
    msg.set_body("微服务开发")
    return msg


def check_callback(msg):
    # TransactionStatus.COMMIT,TransactionStatus.ROLLBACK,TransactionStatus.UNKNOWN
    print(f"事务消息回查：{msg.body.decode('utf-8')}")
    return TransactionStatus.COMMIT


def local_execute(msg, user_args):
    # TransactionStatus.COMMIT,TransactionStatus.ROLLBACK,TransactionStatus.UNKNOWN
    # 这里应该执行业务逻辑，订单表插入
    print("执行本地独立的事务")
    return TransactionStatus.UNKNOWN


def send_transaction_sync(count):
    producer = TransactionMQProducer("test", checker_callback=check_callback)
    producer.set_name_server_address("192.168.1.31:9876")

    # 首先要启动producer
    producer.start()
    for n in range(count):
        msg = create_message()
        ret = producer.send_message_in_transaction(msg, local_execute, None)
        print(f"发生状态：{ret.status},消息id:{ret.msg_id}")
    print("消息发生完成")
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    send_transaction_sync(5)
