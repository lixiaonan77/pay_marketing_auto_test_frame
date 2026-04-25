from tenacity import retry as tenacity_retry, stop_after_attempt, wait_fixed
from config.setting import retry as retry_cfg   # 重命名配置变量

# 读取配置文件中的重试次数和等待时间，提供默认值
MAX_RETRY = retry_cfg.get("max_num", 3) if isinstance(retry_cfg, dict) else 3
WAIT_TIME = retry_cfg.get("wait_time", 1) if isinstance(retry_cfg, dict) else 1

# 自定义异步重试装饰器
def async_retry():
    return tenacity_retry(
        stop=stop_after_attempt(MAX_RETRY),
        wait=wait_fixed(WAIT_TIME)
    )
