# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goods.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0bgoods.proto\x1a\x1bgoogle/protobuf/empty.proto"0\n\x13\x43\x61tegoryListRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05level\x18\x02 \x01(\x05"e\n\x13\x43\x61tegoryInfoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eparentCategory\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\r\n\x05isTab\x18\x05 \x01(\x08"#\n\x15\x44\x65leteCategoryRequest\x12\n\n\x02id\x18\x01 \x01(\x05"0\n\x14QueryCategoryRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"f\n\x14\x43\x61tegoryInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eparentCategory\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\r\n\x05isTab\x18\x05 \x01(\x08"\\\n\x14\x43\x61tegoryListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12#\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x15.CategoryInfoResponse\x12\x10\n\x08jsonData\x18\x03 \x01(\t"z\n\x17SubCategoryListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12#\n\x04info\x18\x02 \x01(\x0b\x32\x15.CategoryInfoResponse\x12+\n\x0csubCategorys\x18\x03 \x03(\x0b\x32\x15.CategoryInfoResponse"@\n\x1a\x43\x61tegoryBrandFilterRequest\x12\r\n\x05pages\x18\x01 \x01(\x05\x12\x13\n\x0bpagePerNums\x18\x02 \x01(\x05"3\n\rFilterRequest\x12\r\n\x05pages\x18\x01 \x01(\x05\x12\x13\n\x0bpagePerNums\x18\x02 \x01(\x05"G\n\x14\x43\x61tegoryBrandRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncategoryId\x18\x02 \x01(\x05\x12\x0f\n\x07\x62randId\x18\x03 \x01(\x05"o\n\x15\x43\x61tegoryBrandResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12!\n\x05\x62rand\x18\x02 \x01(\x0b\x32\x12.BrandInfoResponse\x12\'\n\x08\x63\x61tegory\x18\x03 \x01(\x0b\x32\x15.CategoryInfoResponse"F\n\rBannerRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05image\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t"G\n\x0e\x42\x61nnerResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05image\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t"8\n\x12\x42randFilterRequest\x12\r\n\x05pages\x18\x01 \x01(\x05\x12\x13\n\x0bpagePerNums\x18\x02 \x01(\x05"6\n\x0c\x42randRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04logo\x18\x03 \x01(\t";\n\x11\x42randInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04logo\x18\x03 \x01(\t"D\n\x11\x42randListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.BrandInfoResponse"B\n\x12\x42\x61nnerListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x1d\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x0f.BannerResponse"P\n\x19\x43\x61tegoryBrandListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12$\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x16.CategoryBrandResponse"\x1e\n\x10\x42\x61tchGoodsIdInfo\x12\n\n\x02id\x18\x01 \x03(\x05"\x1d\n\x0f\x44\x65leteGoodsInfo\x12\n\n\x02id\x18\x01 \x01(\x05"5\n\x19\x43\x61tegoryBriefInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"2\n\x15\x43\x61tegoryFilterRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05isTab\x18\x02 \x01(\x08"\x1d\n\x0fGoodInfoRequest\x12\n\n\x02id\x18\x01 \x01(\x05"\xbd\x02\n\x0f\x43reateGoodsInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07goodsSn\x18\x03 \x01(\t\x12\x0e\n\x06stocks\x18\x07 \x01(\x05\x12\x13\n\x0bmarketPrice\x18\x08 \x01(\x02\x12\x11\n\tshopPrice\x18\t \x01(\x02\x12\x12\n\ngoodsBrief\x18\n \x01(\t\x12\x11\n\tgoodsDesc\x18\x0b \x01(\t\x12\x10\n\x08shipFree\x18\x0c \x01(\x08\x12\x0e\n\x06images\x18\r \x03(\t\x12\x12\n\ndescImages\x18\x0e \x03(\t\x12\x17\n\x0fgoodsFrontImage\x18\x0f \x01(\t\x12\r\n\x05isNew\x18\x10 \x01(\x08\x12\r\n\x05isHot\x18\x11 \x01(\x08\x12\x0e\n\x06onSale\x18\x12 \x01(\x08\x12\x12\n\ncategoryId\x18\x13 \x01(\x05\x12\x0f\n\x07\x62randId\x18\x14 \x01(\x05"3\n\x12GoodsReduceRequest\x12\x0f\n\x07GoodsId\x18\x01 \x01(\x05\x12\x0c\n\x04nums\x18\x02 \x01(\x05"L\n\x18\x42\x61tchCategoryInfoRequest\x12\n\n\x02id\x18\x01 \x03(\x05\x12\x11\n\tgoodsNums\x18\x02 \x01(\x05\x12\x11\n\tbrandNums\x18\x03 \x01(\x05"\xcb\x01\n\x12GoodsFilterRequest\x12\x10\n\x08priceMin\x18\x01 \x01(\x05\x12\x10\n\x08priceMax\x18\x02 \x01(\x05\x12\r\n\x05isHot\x18\x03 \x01(\x08\x12\r\n\x05isNew\x18\x04 \x01(\x08\x12\r\n\x05isTab\x18\x05 \x01(\x08\x12\x13\n\x0btopCategory\x18\x06 \x01(\x05\x12\r\n\x05pages\x18\x07 \x01(\x05\x12\x13\n\x0bpagePerNums\x18\x08 \x01(\x05\x12\x10\n\x08keyWords\x18\t \x01(\t\x12\r\n\x05\x62rand\x18\n \x01(\x05\x12\n\n\x02id\x18\x0b \x01(\x05"\xb3\x03\n\x11GoodsInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncategoryId\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07goodsSn\x18\x04 \x01(\t\x12\x10\n\x08\x63lickNum\x18\x05 \x01(\x05\x12\x0f\n\x07soldNum\x18\x06 \x01(\x05\x12\x0e\n\x06\x66\x61vNum\x18\x07 \x01(\x05\x12\x13\n\x0bmarketPrice\x18\t \x01(\x02\x12\x11\n\tshopPrice\x18\n \x01(\x02\x12\x12\n\ngoodsBrief\x18\x0b \x01(\t\x12\x11\n\tgoodsDesc\x18\x0c \x01(\t\x12\x10\n\x08shipFree\x18\r \x01(\x08\x12\x0e\n\x06images\x18\x0e \x03(\t\x12\x12\n\ndescImages\x18\x0f \x03(\t\x12\x17\n\x0fgoodsFrontImage\x18\x10 \x01(\t\x12\r\n\x05isNew\x18\x11 \x01(\x08\x12\r\n\x05isHot\x18\x12 \x01(\x08\x12\x0e\n\x06onSale\x18\x13 \x01(\x08\x12\x0f\n\x07\x61\x64\x64Time\x18\x14 \x01(\x03\x12,\n\x08\x63\x61tegory\x18\x15 \x01(\x0b\x32\x1a.CategoryBriefInfoResponse\x12!\n\x05\x62rand\x18\x16 \x01(\x0b\x32\x12.BrandInfoResponse"D\n\x11GoodsListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.GoodsInfoResponse2\xaf\x0b\n\x05Goods\x12\x34\n\tGoodsList\x12\x13.GoodsFilterRequest\x1a\x12.GoodsListResponse\x12\x36\n\rBatchGetGoods\x12\x11.BatchGoodsIdInfo\x1a\x12.GoodsListResponse\x12\x33\n\x0b\x43reateGoods\x12\x10.CreateGoodsInfo\x1a\x12.GoodsInfoResponse\x12\x37\n\x0b\x44\x65leteGoods\x12\x10.DeleteGoodsInfo\x1a\x16.google.protobuf.Empty\x12\x37\n\x0bUpdateGoods\x12\x10.CreateGoodsInfo\x1a\x16.google.protobuf.Empty\x12\x36\n\x0eGetGoodsDetail\x12\x10.GoodInfoRequest\x1a\x12.GoodsInfoResponse\x12\x44\n\x13GetAllCategorysList\x12\x16.google.protobuf.Empty\x1a\x15.CategoryListResponse\x12@\n\x0eGetSubCategory\x12\x14.CategoryListRequest\x1a\x18.SubCategoryListResponse\x12=\n\x0e\x43reateCategory\x12\x14.CategoryInfoRequest\x1a\x15.CategoryInfoResponse\x12@\n\x0e\x44\x65leteCategory\x12\x16.DeleteCategoryRequest\x1a\x16.google.protobuf.Empty\x12>\n\x0eUpdateCategory\x12\x14.CategoryInfoRequest\x1a\x16.google.protobuf.Empty\x12\x34\n\tBrandList\x12\x13.BrandFilterRequest\x1a\x12.BrandListResponse\x12\x30\n\x0b\x43reateBrand\x12\r.BrandRequest\x1a\x12.BrandInfoResponse\x12\x34\n\x0b\x44\x65leteBrand\x12\r.BrandRequest\x1a\x16.google.protobuf.Empty\x12\x34\n\x0bUpdateBrand\x12\r.BrandRequest\x1a\x16.google.protobuf.Empty\x12\x39\n\nBannerList\x12\x16.google.protobuf.Empty\x1a\x13.BannerListResponse\x12/\n\x0c\x43reateBanner\x12\x0e.BannerRequest\x1a\x0f.BannerResponse\x12\x36\n\x0c\x44\x65leteBanner\x12\x0e.BannerRequest\x1a\x16.google.protobuf.Empty\x12\x36\n\x0cUpdateBanner\x12\x0e.BannerRequest\x1a\x16.google.protobuf.Empty\x12L\n\x11\x43\x61tegoryBrandList\x12\x1b.CategoryBrandFilterRequest\x1a\x1a.CategoryBrandListResponse\x12@\n\x14GetCategoryBrandList\x12\x14.CategoryInfoRequest\x1a\x12.BrandListResponse\x12\x44\n\x13\x43reateCategoryBrand\x12\x15.CategoryBrandRequest\x1a\x16.CategoryBrandResponse\x12\x44\n\x13\x44\x65leteCategoryBrand\x12\x15.CategoryBrandRequest\x1a\x16.google.protobuf.Empty\x12\x44\n\x13UpdateCategoryBrand\x12\x15.CategoryBrandRequest\x1a\x16.google.protobuf.EmptyB\tZ\x07.;protob\x06proto3'
)


_CATEGORYLISTREQUEST = DESCRIPTOR.message_types_by_name["CategoryListRequest"]
_CATEGORYINFOREQUEST = DESCRIPTOR.message_types_by_name["CategoryInfoRequest"]
_DELETECATEGORYREQUEST = DESCRIPTOR.message_types_by_name["DeleteCategoryRequest"]
_QUERYCATEGORYREQUEST = DESCRIPTOR.message_types_by_name["QueryCategoryRequest"]
_CATEGORYINFORESPONSE = DESCRIPTOR.message_types_by_name["CategoryInfoResponse"]
_CATEGORYLISTRESPONSE = DESCRIPTOR.message_types_by_name["CategoryListResponse"]
_SUBCATEGORYLISTRESPONSE = DESCRIPTOR.message_types_by_name["SubCategoryListResponse"]
_CATEGORYBRANDFILTERREQUEST = DESCRIPTOR.message_types_by_name[
    "CategoryBrandFilterRequest"
]
_FILTERREQUEST = DESCRIPTOR.message_types_by_name["FilterRequest"]
_CATEGORYBRANDREQUEST = DESCRIPTOR.message_types_by_name["CategoryBrandRequest"]
_CATEGORYBRANDRESPONSE = DESCRIPTOR.message_types_by_name["CategoryBrandResponse"]
_BANNERREQUEST = DESCRIPTOR.message_types_by_name["BannerRequest"]
_BANNERRESPONSE = DESCRIPTOR.message_types_by_name["BannerResponse"]
_BRANDFILTERREQUEST = DESCRIPTOR.message_types_by_name["BrandFilterRequest"]
_BRANDREQUEST = DESCRIPTOR.message_types_by_name["BrandRequest"]
_BRANDINFORESPONSE = DESCRIPTOR.message_types_by_name["BrandInfoResponse"]
_BRANDLISTRESPONSE = DESCRIPTOR.message_types_by_name["BrandListResponse"]
_BANNERLISTRESPONSE = DESCRIPTOR.message_types_by_name["BannerListResponse"]
_CATEGORYBRANDLISTRESPONSE = DESCRIPTOR.message_types_by_name[
    "CategoryBrandListResponse"
]
_BATCHGOODSIDINFO = DESCRIPTOR.message_types_by_name["BatchGoodsIdInfo"]
_DELETEGOODSINFO = DESCRIPTOR.message_types_by_name["DeleteGoodsInfo"]
_CATEGORYBRIEFINFORESPONSE = DESCRIPTOR.message_types_by_name[
    "CategoryBriefInfoResponse"
]
_CATEGORYFILTERREQUEST = DESCRIPTOR.message_types_by_name["CategoryFilterRequest"]
_GOODINFOREQUEST = DESCRIPTOR.message_types_by_name["GoodInfoRequest"]
_CREATEGOODSINFO = DESCRIPTOR.message_types_by_name["CreateGoodsInfo"]
_GOODSREDUCEREQUEST = DESCRIPTOR.message_types_by_name["GoodsReduceRequest"]
_BATCHCATEGORYINFOREQUEST = DESCRIPTOR.message_types_by_name["BatchCategoryInfoRequest"]
_GOODSFILTERREQUEST = DESCRIPTOR.message_types_by_name["GoodsFilterRequest"]
_GOODSINFORESPONSE = DESCRIPTOR.message_types_by_name["GoodsInfoResponse"]
_GOODSLISTRESPONSE = DESCRIPTOR.message_types_by_name["GoodsListResponse"]
CategoryListRequest = _reflection.GeneratedProtocolMessageType(
    "CategoryListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYLISTREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryListRequest)
    },
)
_sym_db.RegisterMessage(CategoryListRequest)

CategoryInfoRequest = _reflection.GeneratedProtocolMessageType(
    "CategoryInfoRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYINFOREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryInfoRequest)
    },
)
_sym_db.RegisterMessage(CategoryInfoRequest)

DeleteCategoryRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteCategoryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETECATEGORYREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:DeleteCategoryRequest)
    },
)
_sym_db.RegisterMessage(DeleteCategoryRequest)

QueryCategoryRequest = _reflection.GeneratedProtocolMessageType(
    "QueryCategoryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYCATEGORYREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:QueryCategoryRequest)
    },
)
_sym_db.RegisterMessage(QueryCategoryRequest)

CategoryInfoResponse = _reflection.GeneratedProtocolMessageType(
    "CategoryInfoResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYINFORESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryInfoResponse)
    },
)
_sym_db.RegisterMessage(CategoryInfoResponse)

CategoryListResponse = _reflection.GeneratedProtocolMessageType(
    "CategoryListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryListResponse)
    },
)
_sym_db.RegisterMessage(CategoryListResponse)

SubCategoryListResponse = _reflection.GeneratedProtocolMessageType(
    "SubCategoryListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBCATEGORYLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:SubCategoryListResponse)
    },
)
_sym_db.RegisterMessage(SubCategoryListResponse)

CategoryBrandFilterRequest = _reflection.GeneratedProtocolMessageType(
    "CategoryBrandFilterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYBRANDFILTERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryBrandFilterRequest)
    },
)
_sym_db.RegisterMessage(CategoryBrandFilterRequest)

FilterRequest = _reflection.GeneratedProtocolMessageType(
    "FilterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _FILTERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:FilterRequest)
    },
)
_sym_db.RegisterMessage(FilterRequest)

CategoryBrandRequest = _reflection.GeneratedProtocolMessageType(
    "CategoryBrandRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYBRANDREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryBrandRequest)
    },
)
_sym_db.RegisterMessage(CategoryBrandRequest)

CategoryBrandResponse = _reflection.GeneratedProtocolMessageType(
    "CategoryBrandResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYBRANDRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryBrandResponse)
    },
)
_sym_db.RegisterMessage(CategoryBrandResponse)

BannerRequest = _reflection.GeneratedProtocolMessageType(
    "BannerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BANNERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BannerRequest)
    },
)
_sym_db.RegisterMessage(BannerRequest)

BannerResponse = _reflection.GeneratedProtocolMessageType(
    "BannerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BANNERRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BannerResponse)
    },
)
_sym_db.RegisterMessage(BannerResponse)

BrandFilterRequest = _reflection.GeneratedProtocolMessageType(
    "BrandFilterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BRANDFILTERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BrandFilterRequest)
    },
)
_sym_db.RegisterMessage(BrandFilterRequest)

BrandRequest = _reflection.GeneratedProtocolMessageType(
    "BrandRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BRANDREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BrandRequest)
    },
)
_sym_db.RegisterMessage(BrandRequest)

BrandInfoResponse = _reflection.GeneratedProtocolMessageType(
    "BrandInfoResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BRANDINFORESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BrandInfoResponse)
    },
)
_sym_db.RegisterMessage(BrandInfoResponse)

BrandListResponse = _reflection.GeneratedProtocolMessageType(
    "BrandListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BRANDLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BrandListResponse)
    },
)
_sym_db.RegisterMessage(BrandListResponse)

BannerListResponse = _reflection.GeneratedProtocolMessageType(
    "BannerListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BANNERLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BannerListResponse)
    },
)
_sym_db.RegisterMessage(BannerListResponse)

CategoryBrandListResponse = _reflection.GeneratedProtocolMessageType(
    "CategoryBrandListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYBRANDLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryBrandListResponse)
    },
)
_sym_db.RegisterMessage(CategoryBrandListResponse)

BatchGoodsIdInfo = _reflection.GeneratedProtocolMessageType(
    "BatchGoodsIdInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHGOODSIDINFO,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BatchGoodsIdInfo)
    },
)
_sym_db.RegisterMessage(BatchGoodsIdInfo)

DeleteGoodsInfo = _reflection.GeneratedProtocolMessageType(
    "DeleteGoodsInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEGOODSINFO,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:DeleteGoodsInfo)
    },
)
_sym_db.RegisterMessage(DeleteGoodsInfo)

CategoryBriefInfoResponse = _reflection.GeneratedProtocolMessageType(
    "CategoryBriefInfoResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYBRIEFINFORESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryBriefInfoResponse)
    },
)
_sym_db.RegisterMessage(CategoryBriefInfoResponse)

CategoryFilterRequest = _reflection.GeneratedProtocolMessageType(
    "CategoryFilterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CATEGORYFILTERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CategoryFilterRequest)
    },
)
_sym_db.RegisterMessage(CategoryFilterRequest)

GoodInfoRequest = _reflection.GeneratedProtocolMessageType(
    "GoodInfoRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOODINFOREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:GoodInfoRequest)
    },
)
_sym_db.RegisterMessage(GoodInfoRequest)

CreateGoodsInfo = _reflection.GeneratedProtocolMessageType(
    "CreateGoodsInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEGOODSINFO,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:CreateGoodsInfo)
    },
)
_sym_db.RegisterMessage(CreateGoodsInfo)

GoodsReduceRequest = _reflection.GeneratedProtocolMessageType(
    "GoodsReduceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOODSREDUCEREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:GoodsReduceRequest)
    },
)
_sym_db.RegisterMessage(GoodsReduceRequest)

BatchCategoryInfoRequest = _reflection.GeneratedProtocolMessageType(
    "BatchCategoryInfoRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHCATEGORYINFOREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:BatchCategoryInfoRequest)
    },
)
_sym_db.RegisterMessage(BatchCategoryInfoRequest)

GoodsFilterRequest = _reflection.GeneratedProtocolMessageType(
    "GoodsFilterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOODSFILTERREQUEST,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:GoodsFilterRequest)
    },
)
_sym_db.RegisterMessage(GoodsFilterRequest)

GoodsInfoResponse = _reflection.GeneratedProtocolMessageType(
    "GoodsInfoResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOODSINFORESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:GoodsInfoResponse)
    },
)
_sym_db.RegisterMessage(GoodsInfoResponse)

GoodsListResponse = _reflection.GeneratedProtocolMessageType(
    "GoodsListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOODSLISTRESPONSE,
        "__module__": "goods_pb2"
        # @@protoc_insertion_point(class_scope:GoodsListResponse)
    },
)
_sym_db.RegisterMessage(GoodsListResponse)

_GOODS = DESCRIPTOR.services_by_name["Goods"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\007.;proto"
    _CATEGORYLISTREQUEST._serialized_start = 44
    _CATEGORYLISTREQUEST._serialized_end = 92
    _CATEGORYINFOREQUEST._serialized_start = 94
    _CATEGORYINFOREQUEST._serialized_end = 195
    _DELETECATEGORYREQUEST._serialized_start = 197
    _DELETECATEGORYREQUEST._serialized_end = 232
    _QUERYCATEGORYREQUEST._serialized_start = 234
    _QUERYCATEGORYREQUEST._serialized_end = 282
    _CATEGORYINFORESPONSE._serialized_start = 284
    _CATEGORYINFORESPONSE._serialized_end = 386
    _CATEGORYLISTRESPONSE._serialized_start = 388
    _CATEGORYLISTRESPONSE._serialized_end = 480
    _SUBCATEGORYLISTRESPONSE._serialized_start = 482
    _SUBCATEGORYLISTRESPONSE._serialized_end = 604
    _CATEGORYBRANDFILTERREQUEST._serialized_start = 606
    _CATEGORYBRANDFILTERREQUEST._serialized_end = 670
    _FILTERREQUEST._serialized_start = 672
    _FILTERREQUEST._serialized_end = 723
    _CATEGORYBRANDREQUEST._serialized_start = 725
    _CATEGORYBRANDREQUEST._serialized_end = 796
    _CATEGORYBRANDRESPONSE._serialized_start = 798
    _CATEGORYBRANDRESPONSE._serialized_end = 909
    _BANNERREQUEST._serialized_start = 911
    _BANNERREQUEST._serialized_end = 981
    _BANNERRESPONSE._serialized_start = 983
    _BANNERRESPONSE._serialized_end = 1054
    _BRANDFILTERREQUEST._serialized_start = 1056
    _BRANDFILTERREQUEST._serialized_end = 1112
    _BRANDREQUEST._serialized_start = 1114
    _BRANDREQUEST._serialized_end = 1168
    _BRANDINFORESPONSE._serialized_start = 1170
    _BRANDINFORESPONSE._serialized_end = 1229
    _BRANDLISTRESPONSE._serialized_start = 1231
    _BRANDLISTRESPONSE._serialized_end = 1299
    _BANNERLISTRESPONSE._serialized_start = 1301
    _BANNERLISTRESPONSE._serialized_end = 1367
    _CATEGORYBRANDLISTRESPONSE._serialized_start = 1369
    _CATEGORYBRANDLISTRESPONSE._serialized_end = 1449
    _BATCHGOODSIDINFO._serialized_start = 1451
    _BATCHGOODSIDINFO._serialized_end = 1481
    _DELETEGOODSINFO._serialized_start = 1483
    _DELETEGOODSINFO._serialized_end = 1512
    _CATEGORYBRIEFINFORESPONSE._serialized_start = 1514
    _CATEGORYBRIEFINFORESPONSE._serialized_end = 1567
    _CATEGORYFILTERREQUEST._serialized_start = 1569
    _CATEGORYFILTERREQUEST._serialized_end = 1619
    _GOODINFOREQUEST._serialized_start = 1621
    _GOODINFOREQUEST._serialized_end = 1650
    _CREATEGOODSINFO._serialized_start = 1653
    _CREATEGOODSINFO._serialized_end = 1970
    _GOODSREDUCEREQUEST._serialized_start = 1972
    _GOODSREDUCEREQUEST._serialized_end = 2023
    _BATCHCATEGORYINFOREQUEST._serialized_start = 2025
    _BATCHCATEGORYINFOREQUEST._serialized_end = 2101
    _GOODSFILTERREQUEST._serialized_start = 2104
    _GOODSFILTERREQUEST._serialized_end = 2307
    _GOODSINFORESPONSE._serialized_start = 2310
    _GOODSINFORESPONSE._serialized_end = 2745
    _GOODSLISTRESPONSE._serialized_start = 2747
    _GOODSLISTRESPONSE._serialized_end = 2815
    _GOODS._serialized_start = 2818
    _GOODS._serialized_end = 4273
# @@protoc_insertion_point(module_scope)
