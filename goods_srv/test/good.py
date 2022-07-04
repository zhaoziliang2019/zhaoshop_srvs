import json

import consul
import grpc
from google.protobuf import empty_pb2

from goods_srv.proto import goods_pb2, goods_pb2_grpc
from goods_srv.settings import settings


class GoodsTest:
    def __init__(self):
        # 连接grpc服务器
        c = consul.Consul(host="192.168.1.31", port=8500)
        services = c.agent.services()
        ip = ""
        port = ""
        for key, value in services.items():
            if value["Service"] == settings.SERVICE_NAME:
                ip = value["Address"]
                port = value["Port"]
                break
        if not ip:
            raise Exception()
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = goods_pb2_grpc.GoodsStub(channel)

    def goods_list(self):
        rsp: goods_pb2.GoodsListResponse = self.stub.GoodsList(
            goods_pb2.GoodsFilterRequest(topCategory=135485)
        )
        print(rsp.total)
        for item in rsp.data:
            print(item.name, item.shopPrice)

    def batch_get(self):
        ids = [421, 422]
        rsp: goods_pb2.GoodsListResponse = self.stub.GoodsList(
            goods_pb2.BatchGoodsIdInfo(id=ids)
        )
        print(rsp.total)
        for item in rsp.data:
            print(item.name, item.shopPrice)

    def get_detail(self, id):
        rsp = self.stub.GetGoodsDetail(goods_pb2.GoodInfoRequest(id=id))
        print(rsp)

    def category_list(self):
        rsp = self.stub.GetAllCategorysList(empty_pb2.Empty())
        data = json.loads(rsp.jsonData)
        print(data)


if __name__ == "__main__":
    goods = GoodsTest()
    # goods.goods_list()
    # goods.batch_get()
    # goods.get_detail(1)
    goods.category_list()
