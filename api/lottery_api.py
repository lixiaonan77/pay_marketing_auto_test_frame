from common.http_request import http
from config.setting import env
class LotteryApi:
    #发起抽奖
    @staticmethod
    def start_lottery(headers,params):
        url=f"{env[base_url]}/api/lottery/draw"
        return http.send("POST",url,headers=headers,json=params)
    #查奖品库存
    @staticmethod
    def get_prize_stock(headers,prize_name):
        url=f"{env[base_url]}/api/lottery/stock"
        payload={"prize_name":prize_name}
        return http.send("POST",url,headers=headers,json=payload)
    #查中奖记录
    @staticmethod
    def get_win_record(headers,params):
        url=f"{env[base_url]}/api/lottery/record"
        return http.send("GET",url,headers=headers,json=params)
