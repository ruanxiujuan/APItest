"""项目(全局)配置文件"""
import logging
import time
import os


# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
DATA_DIR = os.path.join(BASE_DIR, 'data')  # 数据目录
TEST_DIR = os.path.join(BASE_DIR, 'test_case')
LOG_DIR = os.path.join(BASE_DIR, 'log')
REPORT_DIR = os.path.join(BASE_DIR, 'report')

# 报告配置
REPORT_FILE = os.path.join(REPORT_DIR, 'report.html')
REPORT_TITLE = "我的接口测试报告"
REPORT_DESCRIPTION = '''这是接口测试描述
可以有多行
'''

# 日志配置
TODAY = time.strftime("%Y%m%d", time.localtime(time.time()))
cmd_handler = logging.StreamHandler()
LOG_FILE = os.path.join(LOG_DIR, "{}.log".format(TODAY))
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s %(lineno)d %(funcName)s %(levelname)s %(message)s",
                    handlers=[cmd_handler, file_handler])

# 数据库配置
DB_CONFIG = {
    "host": "115.28.108.130",
    "port": 3306,
    "user": "test",
    "password": "123456",
    "db": "longtengserver",
    "autocommit": True
}