import pika

#建立连接
userx=pika.PlainCredentials("admin","admin")
conn=pika.BlockingConnection(pika.ConnectionParameters(host="172.19.8.230",port=5672,virtual_host='/',credentials=userx))

#开辟管道
channelx=conn.channel()

#声明队列，参数为队列名
#auto_delete队列消费完自动删除该队列，durable持久化
channelx.queue_declare(queue="test2",durable=True,auto_delete=True)

message_str = 'hello world1'
#发送数据，发送一条，如果要发送多条则复制此段
channelx.basic_publish(exchange="",routing_key="test",body=message_str,properties=pika.BasicProperties(delivery_mode=2,))

print("--------发送数据完成-----------")

#关闭连接
conn.close()