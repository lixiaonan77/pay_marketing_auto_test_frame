from common.mq_connect import mq_conn
from config.setting import mq

"""
MQ业务工具类｜放在utils完全合理
理由：
1.不属于框架底层基础
2.是专门为【支付成功后同步业务状态】封装的业务工具
3.发送消息、监听消费 属于业务功能性工具
"""
class MqUtil:

    @staticmethod
    def send_pay_message(order_id,pay_status):
        """
        支付成功后 → MQ生产者发送消息
        :param order_id: 订单id
        :param pay_status: 支付状态 PAY_SUCCESS
        :return:
        """
        # 组装MQ消息体
        msg_body = {
            "orderId":order_id,
            "payStatus":pay_status,
            "msgTip":"支付成功，同步订单状态与用户权益生效"
        }

        # 发送消息到指定队列
        mq_conn.channel.basic_publish(
            exchange="",
            routing_key=mq["queue_name"],
            body=str(msg_body)
        )
        return msg_body


    @staticmethod
    def listen_consume_message():
        """
        MQ消费者：监听队列、消费消息
        消费后自动同步订单状态、权益生效
        """
        result_msg = None

        # 回调函数：收到消息自动执行
        def callback(ch, method, properties, body):
            nonlocal result_msg
            # 解析MQ消息
            result_msg = eval(body.decode())
            # 手动ack确认消费，防止消息丢失
            ch.basic_ack(delivery_tag=method.delivery_tag)

        # 监听队列
        mq_conn.channel.basic_consume(
            queue=mq["queue_name"],
            on_message_callback=callback
        )

        # 只消费一条立刻停止（自动化测试使用）
        mq_conn.channel.start_consuming()
        return result_msg
