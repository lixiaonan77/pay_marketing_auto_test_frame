import pika #1.python中连接RabbitMQ服务(适合支付、订单、业务同步、可靠性要求极高，能保证消息绝不丢失)的专用第三方工具2.创建队列、声明队列3.代码发送MQ消息、监听消费MQ消息
from config.setting import mq
"""
MQ底层连接公共类
职责：统一创建MQ连接、信道、全局服用
属于框架的底层基础 不是业务工具
"""
class MqConnect:
    def __init__(self):
        #MQ连接参数
        self.params=pika.ConnectionParameters(
            host=mq["host"],
            port=mq["port"]
            )
        #创建连接
        self.connection=pika.Connection(self.params)
        #创建信道
        self.channel=self.connection.channel()
        #声明队列(不存在自动创建)
        self.channel.queue_declare(queue=mq["queue_name"],durable=True)
#全局单例MQ连接
mq_conn = MqConnect()
