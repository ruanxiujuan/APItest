import unittest
from HTMLTestReportCN import HTMLTestRunner

# 使用unittest默认的加载器,遍历发现所有test开头py文件中所有Test类中的test开头方法
# 返回一个包含所有用例的测试集合
suite = unittest.defaultTestLoader.discover("./")
# 新建一个执行器
# runner = unittest.TextTestRunner()
# 使用执行器执行测试集合
# runner.run(suite)

# 打开一个文件用来写(wb: 二进制写模式)
f = open("report.html", "wb")
runner = HTMLTestRunner(stream=f, title="接口测报告",
                        description="这个是课堂练习", verbosity=2,
                        tester="赵某某")
runner.run(suite)
f.close()