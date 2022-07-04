import grpc

from user_srv.proto import user_pb2_grpc, user_pb2


class UserTest:
    def __init__(self):
        # 连接grpc服务器
        channle = grpc.insecure_channel(f"192.168.1.15:2121")
        self.stub = user_pb2_grpc.UserStub(channle)

    def user_list(self):
        rsp: user_pb2.UserListResonse = self.stub.GetUserList(
            user_pb2.PageInfo(pn=2, pSize=2)
        )
        print(rsp.total)
        for user in rsp.data:
            print(user.mobile, user.birthDay)

    def get_user_by_id(self, id):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserById(
            user_pb2.IdRequset(id=id)
        )
        print(rsp.mobile, rsp.nickName)

    def create_user(self, mobile, nickName, passWord):
        rsp: user_pb2.UserInfoResponse = self.stub.CreateUser(
            user_pb2.CreateUserInfo(mobile=mobile, nickName=nickName, passWord=passWord)
        )
        print(rsp.mobile, rsp.nickName, rsp.passWord)


if __name__ == "__main__":
    user = UserTest()
    # user.user_list()
    # user.get_user_by_id(105)
    # user.create_user("18710219564","zhaozil","1234567")
    user.create_user("18710219060", "zhaozil", "1234567")
