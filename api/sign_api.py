from common.http_request import http
from config.setting import env

class SignApi:
    #用户每日签到接口
    @staticmethod
    def user_sign(headers,params):
        url=f"{env['base_url']}/api/user/sign"
        return http.send("POST",url,headers=headers,json=params)
    #用户查询当前积分接口
    @staticmethod
    def user_sign(headers,params):
        url=f"{env['base_url']}/api/user/score"
        return http.send("GET",url,headers=headers,json=params)
