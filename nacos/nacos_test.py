from zhaoshop_srvs import nacos
import json
SERVER_ADDRESSES = "192.168.1.26:8848"
NAMESPACE = "a6b026c8-061c-43c7-acf8-0a57b6220030"

# no auth mode
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
# auth mode
#client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")

# get config
data_id = "user-srv.json"
group = "dev"
print(type(client.get_config(data_id, group)))
print(client.get_config(data_id, group))
json_data=json.loads(client.get_config(data_id, group))
print(type(json_data))
print(json_data)
def cb_list(args):
    print("打印配置文件")
    print(args)



if __name__ == '__main__':
    client.add_config_watchers(data_id, group, cb_list)
    import time
    time.sleep(3000)