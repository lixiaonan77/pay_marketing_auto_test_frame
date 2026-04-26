from common.http_request import http
from config.setting import env
from conftest import MOCK_MODE, MockResponse   # 新增导入

class LotteryApi:
    #发起抽奖
    @staticmethod
    def start_lottery(headers,params):
        if MOCK_MODE:
            # 模拟抽奖成功，返回中奖信息
            return MockResponse({"code": 200, "data": {"prize_name": "iPhone 大奖"}})
        url=f"{env['base_url']}/api/lottery/draw"
        return http.send("POST",url,headers=headers,json=params)
    #查奖品库存
    @staticmethod
    def get_prize_stock(headers,prize_name):
        if MOCK_MODE:
            # 模拟库存为1
            return MockResponse({"code": 200, "data": {"stock": 1}})
        url=f"{env['base_url']}/api/lottery/stock"
        payload={"prize_name":prize_name}
        return http.send("POST",url,headers=headers,json=payload)
    #查中奖记录
    @staticmethod
    def get_win_record(headers,params):
         if MOCK_MODE:
            # 模拟中奖记录
            return MockResponse({"code": 200, "data": {"records": []}})
        url=f"{env['base_url]'}/api/lottery/record"
        return http.send("GET",url,headers=headers,json=params)
