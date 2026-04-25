import os
#执行用例并生成allure报告
if __name__ == "__main__":
    #执行自动化
    os.system("pytest testcase/ -vs --alluredir=report/allure-results")
    #生成可视化报告
    os.system("allure generate report/allure-results - o report/allure-html --clean")
