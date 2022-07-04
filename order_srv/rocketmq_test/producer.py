from rocketmq.client import Producer, Message

topic = "TopicTest"


def create_message():
    msg = Message(topic)
    msg.set_keys("zhao")
    msg.set_tags("shop")
    msg.set_delay_time_level(2)
    msg.set_property("name", "services")
    msg.set_body("微服务开发")
    return msg


def send_message_sync(count):
    producer = Producer("test")
    producer.set_name_server_address("192.168.1.31:9876")

    # 首先要启动producer
    producer.start()
    for n in range(count):
        msg = create_message()
        ret = producer.send_sync(msg)
        print(f"发生状态：{ret.status},消息id:{ret.msg_id}")
    print("消息发生完成")
    producer.shutdown()


if __name__ == "__main__":
    send_message_sync(5)
