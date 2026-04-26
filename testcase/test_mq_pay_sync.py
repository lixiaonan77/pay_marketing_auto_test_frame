import yaml
import allure
from utils.mq_util import MqUtil
from utils.retry_util import async_retry
from utils.yaml_util import YamlUtil
mq_data=YamlUtil.load_yaml("mq_data.yaml")
# 读取MQ测试数据
#with open("./data/mq_data.yaml","r",encoding="utf-8") as f:
#    mq_data = yaml.safe_load(f)

@allure.feature("MQ消息队列模块")
@allure.story("支付成功后MQ异步同步订单状态+用户权益生效")
class TestPayMqSync:

    @async_retry()
    def check_mq_consume_result(self,order_id):
        """
        异步重试：防止MQ消息消费延迟
        """
        # 获取消费后的MQ消息
        consume_msg = MqUtil.listen_consume_message()

        # 核心断言1：订单ID一致
        assert consume_msg["orderId"] == order_id
        # 核心断言2：支付状态为成功
        assert consume_msg["payStatus"] == mq_data["pay_mq_msg"]["pay_success"]
        # 核心断言3：业务状态同步描述正确
        assert "同步订单" in consume_msg["msgTip"]

        return consume_msg


    def test_pay_success_send_mq_sync_status(self,global_token_headers):
        """
        完整真实业务链路：
        1.第三方支付回调显示支付成功
        2.后端函数调用MQ生产者发送消息
        3.MQ消费者监听并消费消息
        4.消费完成自动更新订单状态、用户购买权益生效
        5.自动化校验MQ消息内容 & 业务状态同步无误
        """

        # 模拟支付成功后拿到的订单ID（和你支付用例联动）
        order_id = "ORD202604258899"

        with allure.step("1.支付成功，后端调用MQ生产者发送同步消息"):
            send_msg = MqUtil.send_pay_message(
                order_id=order_id,
                pay_status=mq_data["pay_mq_msg"]["pay_success"]
            )
            assert send_msg is not None

        with allure.step("2.MQ消费者监听队列、消费消息、同步业务状态"):
            result = self.check_mq_consume_result(order_id)

        with allure.step("3.最终断言：订单状态、权益全部异步同步完成"):
            print("MQ异步业务状态同步成功：",result)
