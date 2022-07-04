import consul
import grpc

from inventory_srv.proto import inventory_pb2, inventory_pb2_grpc
from inventory_srv.settings import settings


class InventoryTest:
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
        self.stub = inventory_pb2_grpc.InventoryStub(channel)

    def SetInv(self):
        rsp = self.stub.SetInv(inventory_pb2.GoodsInvInfo(goodsId=10, num=100))
        print(rsp)

    def InvDetail(self):
        rsp = self.stub.InvDetail(inventory_pb2.GoodsInvInfo(goodsId=10))
        print(rsp.num)

    def sell(self):
        goods_list = [(10, 20)]
        request = inventory_pb2.SellInfo()
        for goodsId, num in goods_list:
            request.goodsInfo.append(
                inventory_pb2.GoodsInvInfo(goodsId=goodsId, num=num)
            )
        rsp = self.stub.Sell(request)


if __name__ == "__main__":
    inventory = InventoryTest()
    # inventory.SetInv()
    # inventory.InvDetail()
    inventory.sell()
