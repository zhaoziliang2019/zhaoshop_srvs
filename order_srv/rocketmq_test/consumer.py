import time

from rocketmq.client import PushConsumer, ConsumeStatus

topic = "TopicTest"


def callback(msg):
    print(msg.id, msg.body.decode("utf-8"), msg.get_property("name"))
    return ConsumeStatus.CONSUME_SUCCESS


def start_consume_message():
    consumer = PushConsumer("pthon_consumer")
    consumer.set_name_server_address("192.168.1.31:9876")
    consumer.subscribe(topic=topic, callback=callback)
    print("开始消费消息")
    consumer.start()

    while True:
        time.sleep(3600)


if __name__ == "__main__":
    start_consume_message()
