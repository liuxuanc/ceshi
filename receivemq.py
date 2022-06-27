import pika
# import sys
import time

#建立连接
userx=pika.PlainCredentials("admin","admin")
conn=pika.BlockingConnection(pika.ConnectionParameters(host="172.19.8.230",port=5672,virtual_host='/',credentials=userx))

#开辟管道
channelx=conn.channel()

def callback(ch,method,properties,body):
    print(" [%s] Received %r" %(time.time(),body))

channelx.basic_consume(queue='test',on_message_callback=callback,auto_ack=True)
print('xxxx')

channelx.start_consuming()
