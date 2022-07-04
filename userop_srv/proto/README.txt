#命令：
1、pip install grpclib
2、pip3 install grpclib protobuf
3、pip3 install grpcio-tools
4、python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. message.proto
5、python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. address.proto
6、python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. userfav.proto