# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from . import goods_pb2 as goods__pb2


class GoodsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GoodsList = channel.unary_unary(
            "/Goods/GoodsList",
            request_serializer=goods__pb2.GoodsFilterRequest.SerializeToString,
            response_deserializer=goods__pb2.GoodsListResponse.FromString,
        )
        self.BatchGetGoods = channel.unary_unary(
            "/Goods/BatchGetGoods",
            request_serializer=goods__pb2.BatchGoodsIdInfo.SerializeToString,
            response_deserializer=goods__pb2.GoodsListResponse.FromString,
        )
        self.CreateGoods = channel.unary_unary(
            "/Goods/CreateGoods",
            request_serializer=goods__pb2.CreateGoodsInfo.SerializeToString,
            response_deserializer=goods__pb2.GoodsInfoResponse.FromString,
        )
        self.DeleteGoods = channel.unary_unary(
            "/Goods/DeleteGoods",
            request_serializer=goods__pb2.DeleteGoodsInfo.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateGoods = channel.unary_unary(
            "/Goods/UpdateGoods",
            request_serializer=goods__pb2.CreateGoodsInfo.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.GetGoodsDetail = channel.unary_unary(
            "/Goods/GetGoodsDetail",
            request_serializer=goods__pb2.GoodInfoRequest.SerializeToString,
            response_deserializer=goods__pb2.GoodsInfoResponse.FromString,
        )
        self.GetAllCategorysList = channel.unary_unary(
            "/Goods/GetAllCategorysList",
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=goods__pb2.CategoryListResponse.FromString,
        )
        self.GetSubCategory = channel.unary_unary(
            "/Goods/GetSubCategory",
            request_serializer=goods__pb2.CategoryListRequest.SerializeToString,
            response_deserializer=goods__pb2.SubCategoryListResponse.FromString,
        )
        self.CreateCategory = channel.unary_unary(
            "/Goods/CreateCategory",
            request_serializer=goods__pb2.CategoryInfoRequest.SerializeToString,
            response_deserializer=goods__pb2.CategoryInfoResponse.FromString,
        )
        self.DeleteCategory = channel.unary_unary(
            "/Goods/DeleteCategory",
            request_serializer=goods__pb2.DeleteCategoryRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateCategory = channel.unary_unary(
            "/Goods/UpdateCategory",
            request_serializer=goods__pb2.CategoryInfoRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.BrandList = channel.unary_unary(
            "/Goods/BrandList",
            request_serializer=goods__pb2.BrandFilterRequest.SerializeToString,
            response_deserializer=goods__pb2.BrandListResponse.FromString,
        )
        self.CreateBrand = channel.unary_unary(
            "/Goods/CreateBrand",
            request_serializer=goods__pb2.BrandRequest.SerializeToString,
            response_deserializer=goods__pb2.BrandInfoResponse.FromString,
        )
        self.DeleteBrand = channel.unary_unary(
            "/Goods/DeleteBrand",
            request_serializer=goods__pb2.BrandRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateBrand = channel.unary_unary(
            "/Goods/UpdateBrand",
            request_serializer=goods__pb2.BrandRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.BannerList = channel.unary_unary(
            "/Goods/BannerList",
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=goods__pb2.BannerListResponse.FromString,
        )
        self.CreateBanner = channel.unary_unary(
            "/Goods/CreateBanner",
            request_serializer=goods__pb2.BannerRequest.SerializeToString,
            response_deserializer=goods__pb2.BannerResponse.FromString,
        )
        self.DeleteBanner = channel.unary_unary(
            "/Goods/DeleteBanner",
            request_serializer=goods__pb2.BannerRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateBanner = channel.unary_unary(
            "/Goods/UpdateBanner",
            request_serializer=goods__pb2.BannerRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CategoryBrandList = channel.unary_unary(
            "/Goods/CategoryBrandList",
            request_serializer=goods__pb2.CategoryBrandFilterRequest.SerializeToString,
            response_deserializer=goods__pb2.CategoryBrandListResponse.FromString,
        )
        self.GetCategoryBrandList = channel.unary_unary(
            "/Goods/GetCategoryBrandList",
            request_serializer=goods__pb2.CategoryInfoRequest.SerializeToString,
            response_deserializer=goods__pb2.BrandListResponse.FromString,
        )
        self.CreateCategoryBrand = channel.unary_unary(
            "/Goods/CreateCategoryBrand",
            request_serializer=goods__pb2.CategoryBrandRequest.SerializeToString,
            response_deserializer=goods__pb2.CategoryBrandResponse.FromString,
        )
        self.DeleteCategoryBrand = channel.unary_unary(
            "/Goods/DeleteCategoryBrand",
            request_serializer=goods__pb2.CategoryBrandRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateCategoryBrand = channel.unary_unary(
            "/Goods/UpdateCategoryBrand",
            request_serializer=goods__pb2.CategoryBrandRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class GoodsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GoodsList(self, request, context):
        """商品接口"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchGetGoods(self, request, context):
        """现在用户提交订单有多个商品，你得批量查询商品的信息吧
        批量获取商品信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateGoods(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteGoods(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateGoods(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetGoodsDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAllCategorysList(self, request, context):
        """商品分类
        获取所有的分类
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSubCategory(self, request, context):
        """获取子分类"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateCategory(self, request, context):
        """新建分类信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteCategory(self, request, context):
        """删除分类"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateCategory(self, request, context):
        """修改分类信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BrandList(self, request, context):
        """品牌和轮播图
        批量获取品牌信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateBrand(self, request, context):
        """新建品牌信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteBrand(self, request, context):
        """删除品牌"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateBrand(self, request, context):
        """修改品牌信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BannerList(self, request, context):
        """轮播图
        获取轮播列表信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateBanner(self, request, context):
        """添加banner图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteBanner(self, request, context):
        """删除轮播图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateBanner(self, request, context):
        """修改轮播图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CategoryBrandList(self, request, context):
        """品牌分类
        获取轮播列表信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCategoryBrandList(self, request, context):
        """通过category获取brands"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateCategoryBrand(self, request, context):
        """添加banner图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteCategoryBrand(self, request, context):
        """删除轮播图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateCategoryBrand(self, request, context):
        """修改轮播图"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GoodsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GoodsList": grpc.unary_unary_rpc_method_handler(
            servicer.GoodsList,
            request_deserializer=goods__pb2.GoodsFilterRequest.FromString,
            response_serializer=goods__pb2.GoodsListResponse.SerializeToString,
        ),
        "BatchGetGoods": grpc.unary_unary_rpc_method_handler(
            servicer.BatchGetGoods,
            request_deserializer=goods__pb2.BatchGoodsIdInfo.FromString,
            response_serializer=goods__pb2.GoodsListResponse.SerializeToString,
        ),
        "CreateGoods": grpc.unary_unary_rpc_method_handler(
            servicer.CreateGoods,
            request_deserializer=goods__pb2.CreateGoodsInfo.FromString,
            response_serializer=goods__pb2.GoodsInfoResponse.SerializeToString,
        ),
        "DeleteGoods": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteGoods,
            request_deserializer=goods__pb2.DeleteGoodsInfo.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateGoods": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateGoods,
            request_deserializer=goods__pb2.CreateGoodsInfo.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "GetGoodsDetail": grpc.unary_unary_rpc_method_handler(
            servicer.GetGoodsDetail,
            request_deserializer=goods__pb2.GoodInfoRequest.FromString,
            response_serializer=goods__pb2.GoodsInfoResponse.SerializeToString,
        ),
        "GetAllCategorysList": grpc.unary_unary_rpc_method_handler(
            servicer.GetAllCategorysList,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=goods__pb2.CategoryListResponse.SerializeToString,
        ),
        "GetSubCategory": grpc.unary_unary_rpc_method_handler(
            servicer.GetSubCategory,
            request_deserializer=goods__pb2.CategoryListRequest.FromString,
            response_serializer=goods__pb2.SubCategoryListResponse.SerializeToString,
        ),
        "CreateCategory": grpc.unary_unary_rpc_method_handler(
            servicer.CreateCategory,
            request_deserializer=goods__pb2.CategoryInfoRequest.FromString,
            response_serializer=goods__pb2.CategoryInfoResponse.SerializeToString,
        ),
        "DeleteCategory": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCategory,
            request_deserializer=goods__pb2.DeleteCategoryRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateCategory": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCategory,
            request_deserializer=goods__pb2.CategoryInfoRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "BrandList": grpc.unary_unary_rpc_method_handler(
            servicer.BrandList,
            request_deserializer=goods__pb2.BrandFilterRequest.FromString,
            response_serializer=goods__pb2.BrandListResponse.SerializeToString,
        ),
        "CreateBrand": grpc.unary_unary_rpc_method_handler(
            servicer.CreateBrand,
            request_deserializer=goods__pb2.BrandRequest.FromString,
            response_serializer=goods__pb2.BrandInfoResponse.SerializeToString,
        ),
        "DeleteBrand": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBrand,
            request_deserializer=goods__pb2.BrandRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateBrand": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBrand,
            request_deserializer=goods__pb2.BrandRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "BannerList": grpc.unary_unary_rpc_method_handler(
            servicer.BannerList,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=goods__pb2.BannerListResponse.SerializeToString,
        ),
        "CreateBanner": grpc.unary_unary_rpc_method_handler(
            servicer.CreateBanner,
            request_deserializer=goods__pb2.BannerRequest.FromString,
            response_serializer=goods__pb2.BannerResponse.SerializeToString,
        ),
        "DeleteBanner": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBanner,
            request_deserializer=goods__pb2.BannerRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateBanner": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBanner,
            request_deserializer=goods__pb2.BannerRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CategoryBrandList": grpc.unary_unary_rpc_method_handler(
            servicer.CategoryBrandList,
            request_deserializer=goods__pb2.CategoryBrandFilterRequest.FromString,
            response_serializer=goods__pb2.CategoryBrandListResponse.SerializeToString,
        ),
        "GetCategoryBrandList": grpc.unary_unary_rpc_method_handler(
            servicer.GetCategoryBrandList,
            request_deserializer=goods__pb2.CategoryInfoRequest.FromString,
            response_serializer=goods__pb2.BrandListResponse.SerializeToString,
        ),
        "CreateCategoryBrand": grpc.unary_unary_rpc_method_handler(
            servicer.CreateCategoryBrand,
            request_deserializer=goods__pb2.CategoryBrandRequest.FromString,
            response_serializer=goods__pb2.CategoryBrandResponse.SerializeToString,
        ),
        "DeleteCategoryBrand": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCategoryBrand,
            request_deserializer=goods__pb2.CategoryBrandRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "UpdateCategoryBrand": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCategoryBrand,
            request_deserializer=goods__pb2.CategoryBrandRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("Goods", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Goods(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GoodsList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/GoodsList",
            goods__pb2.GoodsFilterRequest.SerializeToString,
            goods__pb2.GoodsListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BatchGetGoods(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/BatchGetGoods",
            goods__pb2.BatchGoodsIdInfo.SerializeToString,
            goods__pb2.GoodsListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateGoods(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CreateGoods",
            goods__pb2.CreateGoodsInfo.SerializeToString,
            goods__pb2.GoodsInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteGoods(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/DeleteGoods",
            goods__pb2.DeleteGoodsInfo.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateGoods(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/UpdateGoods",
            goods__pb2.CreateGoodsInfo.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetGoodsDetail(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/GetGoodsDetail",
            goods__pb2.GoodInfoRequest.SerializeToString,
            goods__pb2.GoodsInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetAllCategorysList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/GetAllCategorysList",
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            goods__pb2.CategoryListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetSubCategory(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/GetSubCategory",
            goods__pb2.CategoryListRequest.SerializeToString,
            goods__pb2.SubCategoryListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateCategory(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CreateCategory",
            goods__pb2.CategoryInfoRequest.SerializeToString,
            goods__pb2.CategoryInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteCategory(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/DeleteCategory",
            goods__pb2.DeleteCategoryRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateCategory(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/UpdateCategory",
            goods__pb2.CategoryInfoRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BrandList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/BrandList",
            goods__pb2.BrandFilterRequest.SerializeToString,
            goods__pb2.BrandListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CreateBrand",
            goods__pb2.BrandRequest.SerializeToString,
            goods__pb2.BrandInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/DeleteBrand",
            goods__pb2.BrandRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/UpdateBrand",
            goods__pb2.BrandRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BannerList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/BannerList",
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            goods__pb2.BannerListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateBanner(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CreateBanner",
            goods__pb2.BannerRequest.SerializeToString,
            goods__pb2.BannerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteBanner(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/DeleteBanner",
            goods__pb2.BannerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateBanner(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/UpdateBanner",
            goods__pb2.BannerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CategoryBrandList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CategoryBrandList",
            goods__pb2.CategoryBrandFilterRequest.SerializeToString,
            goods__pb2.CategoryBrandListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCategoryBrandList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/GetCategoryBrandList",
            goods__pb2.CategoryInfoRequest.SerializeToString,
            goods__pb2.BrandListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateCategoryBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/CreateCategoryBrand",
            goods__pb2.CategoryBrandRequest.SerializeToString,
            goods__pb2.CategoryBrandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteCategoryBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/DeleteCategoryBrand",
            goods__pb2.CategoryBrandRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateCategoryBrand(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Goods/UpdateCategoryBrand",
            goods__pb2.CategoryBrandRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
