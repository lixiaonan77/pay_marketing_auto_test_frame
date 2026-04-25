import os
import yaml

# 获取 setting.yaml 的绝对路径
cur_dir = os.path.dirname(__file__)
yaml_path = os.path.join(cur_dir, 'setting.yaml')

# 读取 YAML 文件
with open(yaml_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 如果 config 为 None 或空，说明 YAML 文件无法解析，请检查文件格式
if config is None:
    raise ValueError(f"Failed to parse YAML file: {yaml_path}")

# 导出变量（确保是字典，如果 YAML 中没有对应键则设为空字典）
env = config.get('env', {})
login_user = config.get('login_user', {})
retry = config.get('retry', {})
mq = config.get('mq', {})

