from common.http_request import http
from config.setting import env, login_user


class LoginApi:
    #登录接口：全局获取token
    @staticmethod
    def login():
        url=f"{env['base_url']}/api/user/login"
        payload={
            "username":login_user["username"],
            "password":login_user["password"],

        }
        return http.send("POST",url,json=payload)
