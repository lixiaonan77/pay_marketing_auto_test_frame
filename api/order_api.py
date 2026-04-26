from common.http_request import http
from config.setting import env
from conftest import MOCK_MODE, MockResponse   # 新增导入mock用

class OrderApi:
    #创建订单接口
    @staticmethod
    def create_goods_order(headers,goods_id,amount):
        if MOCK_MODE:
            # 模拟创建订单成功，返回订单ID
            return MockResponse({"code": 200, "data": {"orderId": 123456}})
        url=f"{env['base_url']}/api/order/create"
        data={
            "goodsId":goods_id,
            "amount":amount
        }
        return http.send("POST",url,headers=headers,json=data)
    
