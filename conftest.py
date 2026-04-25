import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
import pytest
from api.login_api import LoginApi
#会话级别：整个项目运行只登录一次，所有用例共享token
@pytest.fixture(scope="session")
def global_headers():
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
