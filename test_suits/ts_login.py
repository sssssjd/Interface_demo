# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 16:57
# @Author  : sssssjd
# @Email   : sssssjd@163.com
# @File    : ts_login.py
# @Software: PyCharm

import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # tests = [TestLogin("test_login")]
    # suite.addTest(TestLogin("test_login"))

    # 直接用addTest方法添加单个TestCase
    # suite.addTest(TestMathFunc("test_multi"))

    # 用addTests + TestLoader
    # loadTestsFromName()，传入'模块名.TestCase名'
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    # loadTestsFromNames()，类似，传入列表
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    test_dir = r'C:\Users\faqkingphone1\PycharmProjects\Interface_demo\test_cases'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='tc_*.py')
    nowtime = time.localtime(time.time())
    nowtime = time.strftime("%Y%m%d-%H%M", nowtime)
    file_location = 'C://Users//faqkingphone1//PycharmProjects//' \
                    'Interface_demo//test_result//html_report//ts_login-' + nowtime + '.html'

    with open(file_location, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='TestLogin Report',
                                description='人人说登录接口测试',
                                tester='ssssjd',
                                verbosity=2
                                )
        runner.run(discover)
