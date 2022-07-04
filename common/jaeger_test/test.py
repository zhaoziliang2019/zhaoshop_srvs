import logging
import random
import time

import requests
from jaeger_client import Config

if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(asctime)s %(message)s", level=log_level)

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
        service_name="zhaoshop",
        validate=True,
    )
    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()
    with tracer.start_span("spider") as spider_span:
        with tracer.start_span("get", child_of=spider_span) as get_span:
            requests.get("https://www.baidu.com")
        with tracer.start_span("parser", child_of=spider_span) as parser_span:
            time.sleep(random.randint(1, 9) * 0.1)

    time.sleep(
        2
    )  # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()  # flush any buffered spans
