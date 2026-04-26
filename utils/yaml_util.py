import os
import yaml
from pathlib import Path

# 获取项目根目录（假设 utils 目录在项目根目录下）
ROOT_DIR = Path(__file__).parent.parent

class YamlUtil:
    """YAML 文件读取工具"""
    
    @staticmethod
    def load_yaml(file_name: str, data_dir: str = "data") -> dict:
        """
        读取 data 目录下的 YAML 文件
        :param file_name: 文件名，如 "pay_data.yaml"
        :param data_dir: 数据目录名，默认为 "data"
        :return: 解析后的字典
        """
        file_path = ROOT_DIR / data_dir / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"YAML 文件不存在: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_data(file_name: str, key: str = None):
        """
        读取 YAML 文件，可选择返回某个键对应的值
        :param file_name: 文件名
        :param key: 若提供，则返回 data[key]；否则返回全部数据
        """
        data = YamlUtil.load_yaml(file_name)
        if key is not None:
            return data.get(key)
        return data
