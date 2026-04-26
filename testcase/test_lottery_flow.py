import yaml
import allure
from api.lottery_api import LotteryApi
from utils.retry_util import async_retry

# 读取抽奖限制规则
with open("./data/lottery_data.yaml", "r", encoding="utf-8") as f:
    lottery_data = yaml.safe_load(f)

@allure.feature("抽奖活动模块")
@allure.story("iPhone大奖｜库存唯一 + 30天限中奖1次 + 有效期30天")
class TestIphoneLotteryRule:

    # 异步重试：轮询中奖记录、校验业务规则
    @async_retry()
    def check_lottery_win_rule(self, headers,prize_name):
        rule = lottery_data["lottery_rule"]
        res = LotteryApi.get_win_record(headers,prize_name)
        win_list = res.json()["data"]["list"]

        # 遍历中奖记录，强校验所有需求规则
        for item in win_list:
            if item["prizeName"] == rule["prize_name"]:
                # 校验1：奖品库存只有1个
                assert item["stock"] == rule["stock_limit"]
                # 校验2：30天只能中奖一次
                assert item["limitDays"] == rule["limit_days"]
                # 校验3：中奖有效期30天
                assert item["validDays"] == rule["prize_valid_days"]
                return True
        # 没查到中奖记录就抛异常，自动触发重试
        raise Exception("未查询到中奖记录，继续轮询")

    def test_lottery_full_business(self, global_token_headers):
        headers= global_token_headers
        rule_params = lottery_data["lottery_rule"]

        with allure.step("1.校验iPhone大奖库存严格为1"):
            stock_res = LotteryApi.get_prize_stock(headers, rule_params["prize_name"])
            assert stock_res.json()["data"]["stock"] == rule_params["stock_limit"]

        with allure.step("2.用户发起抽奖"):
            LotteryApi.start_lottery(headers, rule_params)

        with allure.step("3.校验30天中奖限制 + 奖品有效期"):
            self.check_lottery_win_rule(headers, rule_params["prize_name"])
