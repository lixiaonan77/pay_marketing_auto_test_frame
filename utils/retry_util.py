from tenacity import retry,stop_after_attempt,wait_fixed
from config.setting importretry
#读取配置文件重试次数&等待时间
MAX_RETRY=retry["max_num"]
WAIT_TIME=retry["wait_time"]
#自定义异步重试装饰器
#适用：支付回调、抽奖结果查询等异步延迟场景
def async_retry():
    return retry(
        stop=stop_after_attempt(MAX_RETRY),
        wait=wait_fixed(WAIT_TIME)
    )
