import pika
import time
from config.setting import mq

class MqConnect:
    def __init__(self, retry=5, delay=2):
        # 修正端口为 5672（RabbitMQ 默认端口）
        host = mq.get("host", "127.0.0.1")
        port = mq.get("port", 5672)
        queue_name = mq.get("queue_name", "pay_order_status_queue")

        self.params = pika.ConnectionParameters(host=host, port=port)

        # 重试连接，避免 CI 环境服务未完全启动
        for attempt in range(retry):
            try:
                self.connection = pika.BlockingConnection(self.params)
                break
            except pika.exceptions.AMQPConnectionError as e:
                if attempt == retry - 1:
                    raise Exception(f"无法连接 RabbitMQ ({host}:{port})，请确认服务已启动。原始错误: {e}")
                time.sleep(delay)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)


# 延迟初始化：只在第一次访问时创建连接
_mq_conn_instance = None

def _get_mq_conn():
    global _mq_conn_instance
    if _mq_conn_instance is None:
        _mq_conn_instance = MqConnect()
    return _mq_conn_instance


# 代理类：使得 mq_conn 的使用方式完全不变，但只有在真正访问属性时才创建连接
class _LazyMqConn:
    def __getattr__(self, name):
        return getattr(_get_mq_conn(), name)


# 兼容原有导入：from common.mq_connect import mq_conn
mq_conn = _LazyMqConn()
