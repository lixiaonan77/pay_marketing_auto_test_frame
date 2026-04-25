import yaml
import allure
from api.order_api import OrderApi
from api.pay_api import PayApi
from utils.retry_util import async_retry

# 读取支付测试数据
with open("./data/pay_data.yaml", "r", encoding="utf-8") as f:
    pay_data = yaml.safe_load(f)

@allure.feature("支付中心模块")
@allure.story("创建订单 + 唤起第三方支付 + 异步回调结果校验")
class TestThirdPayBusiness:

    # 支付结果异步轮询重试
    @async_retry()
    def check_pay_success(self, headers, order_id):
        res = PayApi.query_pay_status(headers, order_id)
        assert res.json()["code"] == 200
        # 支付未成功主动抛出异常，触发重试
        if res.json()["data"]["payStatus"] != "PAY_SUCCESS":
            raise Exception("第三方支付未回调，等待重试")

    def test_pay_all_flow(self, global_token_headers):
        headers = global_token_headers
        data = pay_data

        with allure.step("1.创建商品订单"):
            order_res = OrderApi.create_goods_order(
                headers=headers,
                goods_id=data["order_info"]["goods_id"],
                amount=data["order_info"]["goods_amount"]
            )
            order_id = order_res.json()["data"]["orderId"]
            assert order_id

        with allure.step("2.调用第三方支付宝支付"):
            PayApi.third_pay_call(
                headers=headers,
                order_id=order_id,
                pay_type=data["pay_info"]["pay_type"]
            )

        with allure.step("3.异步重试等待回调，最终断言支付成功"):
            self.check_pay_success(headers, order_id)
