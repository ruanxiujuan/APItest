import unittest
# from test_login2 import TestLogin2, TestReg2
# import test_login2
#
# # 新建测试套件(组织用例)
# suite = unittest.TestSuite()
# # 逐条添加
# suite.addTest(TestLogin2("test_login"))
# suite.addTest(TestReg2("test_reg"))
# # 批量添加
# suite.addTests([TestLogin2("test_login"),TestReg2("test_reg")])
#
# suite1 = unittest.TestSuite()
# suite1.addTest(TestLogin2("test_login"))
# suite2 = unittest.TestSuite()
# suite2.addTest(TestReg2("test_reg"))
#
# suite3 = unittest.TestSuite()
# suite3.addTests([suite1,suite2])
# print(suite1, suite2)
# print(suite3)
#
# loader = unittest.TestLoader()
# suite4 = loader.loadTestsFromModule(test_login2)
#
# print(suite4)

# 新建一个执行器


suite = unittest.defaultTestLoader.discover("./")
unittest.TextTestRunner(verbosity=2).run(suite)
