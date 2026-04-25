from common.http_request import http
from config.setting import env
class PayApi:
    #调用第三方支付接口
    @staticmethod
    def third_pay(headers,order_id,pay_type):
        url=f"{env[base_url]/api/pay/third}"
        data={"orderId":order_id,"payType":pay_type}
        return http.send("POST",url,headers=headers,json=data)
    #查询支付状态接口
    @staticmethod
    def get_pay_status(headers,order_ide):
        url=f"{env[base_url]/api/order/pay/status}"
        data={"orderId":order_id,}
        return http.send("GET",url,headers=headers,json=data)
