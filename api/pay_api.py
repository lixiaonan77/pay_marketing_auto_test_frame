from common.http_request import http
from config.setting import env
from conftest import MOCK_MODE, MockResponse   # 新增导入mock用

class PayApi:
    # 调用第三方支付接口
    @staticmethod
    def third_pay_call(headers, order_id, pay_type):
        if MOCK_MODE:
            return MockResponse({"code": 200, "message": "支付调用成功"})
        url = f"{env['base_url']}/api/pay/third"
        data = {"orderId": order_id, "payType": pay_type}
        return http.send("POST", url, headers=headers, json=data)

    # 查询支付状态接口
    @staticmethod
    def query_pay_status(headers, order_id):
        if MOCK_MODE:
            return MockResponse({"code": 200, "data": {"payStatus": "PAY_SUCCESS"}})
        url = f"{env['base_url']}/api/order/pay/status"
        data = {"orderId": order_id}
        return http.send("GET", url, headers=headers, json=data)
