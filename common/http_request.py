import requests
#统一请求封装类 全局共用、减少代码冗余
class HttpRequest:
    def __init__(self):
    #保持会话自动携带cookie
        self.session = requests.Session() #让后端识别是同一个客户端、不拦截、链路连贯、请求稳定
    def send(self,method,url,headers=None,json=None):
        """
        :param method:请求方式 GET/POST
        :param url:接口地址
        :param headers:请求头token，证明你是谁，有没有权限
        :param json:请求体参数
        :return:接口响应对象
        """
        res=self.session.request(
            method=method,
            url=url,
            headers=headers,
            json=params,
            timeout=15
        )
        return res
#全局单列对象 全程只用一个请求实例
http=HttpRequest()
