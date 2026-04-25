from common.http_request import http
from config.setting import env
class OrderApi:
    #创建订单接口
    @staticmethod
    def create_order(headers,good_id,amount):
        url=f"{env[base_url]}/api/order/create"
        data={
            "goodsId":good_id,
            "amount":amount
        }
        return http.send("POST",url,headers=headers,json=data)
    
