import pika
import sys

userx=pika.PlainCredentials("admin","admin")
conn=pika.BlockingConnection(pika.ConnectionParameters(host="172.19.8.230",port=5672,virtual_host='/',credentials=userx))

channel = conn.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout',durable=True)


# exclusive 不指定queue名字 ，rabbitmq会随机分一个，exclusive会在使用此queue的消费者
# 断开后，自动将queue删除
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue  # 取到queue名字
# print("random queue1", queue_name)


# 绑定转发器，让发送端知道是哪个queue
channel.queue_bind(exchange='logs',
                   queue='queue3')
print(' [*] Waiting for logs, To exit press CRTL +C')


def callback(ch, method, properties, body):
    print("[x] %r" % body)

#让发送端知道是哪个queue，如果是随机的则queue_name
channel.basic_consume(queue='dxsd',on_message_callback=callback,auto_ack=True)  # 不确认消息
channel.start_consuming()