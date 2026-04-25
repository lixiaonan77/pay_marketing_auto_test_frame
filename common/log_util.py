import logging
#日志统一配置 打印执行过程与错误信息 不加basicConfig日志格式会特别乱 只打印内容，没有时间、级别、排版乱、默认级别是WARNNG
logging.basicConfig(
    lever=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
    )
#getLogger()拿一个日志工具 它本身没有任何格式
logger =logging.getLogger()
