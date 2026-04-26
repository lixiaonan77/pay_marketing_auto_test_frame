import yaml
import allure
from api.sign_api import SignApi
#读取签到测试数据
with open("./data/sign_data.yaml","r",encoding="utf-8") as f:
    sign_data=yaml.safe_load(f)
@allure.feature("用户模块")
@allure.story("每日签到+积分获取流程")
class TestSignBusiness:
    def test_user_sign_add_score(self,global_token_headers):
        """
        业务流程：
        1.用户执行每日签到
        2.校验签到成功
        3.查询积分，验证积分正常增加
        """
        headers=global_token_headers
        sign_params=sign_data["sign_params"]
        expect_score=sign_data["expect_score"]
        with allure.step("1.用户发起每日签到操作"):
            sign_res=SignApi.user_sign(headers=headers,params=sign_params)
            #断言签到接口正常
            assert sign_res.status_code == 200
            assert sign_res.json()["code"] == 200
        with allure.step("2.查询用户积分，验证积分到账功能"):
            score_res=SignApi.get_user_score(headers=headers,params=sign_params)
            #断言查询接口正常，返回包含score字段，断言签到后总积分和预期中积分一致
            assert score_res.status_code == 200
            assert "score" in score_res.json()["data"]
            assert score_res.json()["data"]["score"] == expect_score

