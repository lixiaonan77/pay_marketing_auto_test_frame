import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))  

import pytest
import os

# 1. 执行用例，生成allure原始数据
pytest.main(["-vs", "--alluredir=report/allure-results"])

# 2. 生成allure html报告
os.system("allure generate report/allure-results -o report/allure-html --clean")

# 3. 打开报告
os.system("allure open report/allure-html")
