import pika
import sys

#建立连接
userx=pika.PlainCredentials("admin","admin")
conn=pika.BlockingConnection(pika.ConnectionParameters(host="172.19.8.230",port=5672,virtual_host='/',credentials=userx))

#开辟管道
channel=conn.channel()

#durable=True清空不删除
channel.exchange_declare(exchange='logs',exchange_type='fanout',durable=True)

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
#发送数据，发送一条，如果要发送多条则复制此段

channel.basic_publish(exchange='logs',routing_key='',body=message)

print("[x] Sent %r"%message)

#关闭连接
conn.close()