from common.http_request import http
from config.setting import env
from conftest import MOCK_MODE, MockResponse   # 新增导入

class SignApi:
    # 用户每日签到接口
    @staticmethod
    def user_sign(headers, params):
        if MOCK_MODE:
            # 模拟签到成功，返回增加后的积分
            return MockResponse({"code": 200, "data": {"score": 10}})
        url = f"{env['base_url']}/api/user/sign"
        return http.send("POST", url, headers=headers, params=params)

    # 用户查询当前积分接口
    @staticmethod
    def get_user_score(headers, params):
        if MOCK_MODE:
            # 模拟当前积分
            return MockResponse({"code": 200, "data": {"score": 10}})
        url = f"{env['base_url']}/api/user/score"
        
        return http.send("GET", url, headers=headers,params=params)
