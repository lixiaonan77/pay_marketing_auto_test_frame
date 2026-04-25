# utils/mq_util.py
import json
from common.mq_connect import mq_conn
from config.setting import mq

class MqUtil:

    @staticmethod
    def send_pay_message(order_id, pay_status):
        """发送支付成功消息（生产者）"""
        msg_body = {
            "orderId": order_id,
            "payStatus": pay_status,
            "msgTip": "支付成功，同步订单状态与用户权益生效"
        }
        # 使用 json.dumps 生成标准字符串
        message_str = json.dumps(msg_body, ensure_ascii=False)
        mq_conn.channel.basic_publish(
            exchange="",
            routing_key=mq["queue_name"],
            body=message_str.encode('utf-8')
        )
        return msg_body

    @staticmethod
    def listen_consume_message():
        """消费一条消息后自动停止（非阻塞拉取）"""
        # 方法1：使用 basic_get 主动拉取（推荐，简单可控）
        method_frame, header_frame, body = mq_conn.channel.basic_get(
            queue=mq["queue_name"], 
            auto_ack=False
        )
        if method_frame:
            # 解析消息
            message = json.loads(body.decode('utf-8'))
            # 手动 ack
            mq_conn.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            return message
        else:
            # 队列无消息时返回 None
            return None

    # 如果你仍希望使用回调 + start_consuming 方式（慎用，会阻塞）
    @staticmethod
    def listen_consume_message_blocking():
        """阻塞消费一条消息（仅用于单独脚本测试）"""
        result = None

        def callback(ch, method, properties, body):
            nonlocal result
            result = json.loads(body.decode('utf-8'))
            ch.basic_ack(delivery_tag=method.delivery_tag)
            ch.stop_consuming()   # 关键：消费一条后停止

        mq_conn.channel.basic_consume(
            queue=mq["queue_name"],
            on_message_callback=callback,
            auto_ack=False
        )
        mq_conn.channel.start_consuming()   # 阻塞，直到 stop_consuming 被调用
        return result
