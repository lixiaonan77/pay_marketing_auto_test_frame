import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
import pytest
from api.login_api import LoginApi
#会话级别：整个项目运行只登录一次，所有用例共享token
@pytest.fixture(scope="session")
def global_token_headers():
    # 如果设置了 MOCK_LOGIN 环境变量，则跳过真实登录
    if os.getenv("MOCK_LOGIN"):
        return {
            "Authorization": "mock-token-for-ci",
            "Content-Type": "application/json"
        }
    #执行登录
    login_res=LoginApi.login()
    #提取token
    token=login_res.json()["data"]["token"]
    #统一请求头
    headers={
        "Authorization": token,
        "Content-Type": "application/json"
    }
    return headers
