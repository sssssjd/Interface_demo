# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 11:19
# @Author  : sssssjd
# @Email   : sssssjd@163.com
# @File    : tc_login.py
# @Software: PyCharm
import requests
import unittest
import ddt
import json
import logging
from common.operating_data import getdata_xlsx

registerdata = getdata_xlsx.get_xlsxdata('C://Users//faqkingphone1//PycharmProjects//'
                                     'Interface_demo//test_data//login_data.xlsx', '注册接口')
logindata = getdata_xlsx.get_xlsxdata('C://Users//faqkingphone1//PycharmProjects//'
                                     'Interface_demo//test_data//login_data.xlsx', '登录接口')
logging.basicConfig(filename='C://Users//faqkingphone1//PycharmProjects//'
                             'Interface_demo//test_result//log1.log', level=logging.INFO)


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('start...')

    def tearDown(self):
        print('end...')

    @ddt.data(*logindata)
    def test_login(self, data):
        """人人说前端用户登录测试"""
        rq_method = data['method']
        url = data['url']
        if data['params']:
            params = json.loads(data['params'])
        else:
            params = ''
        headers = json.loads(data['headers'])
        response = requests.request(rq_method, url, headers=headers, params=params)
        if response.status_code != 200:
            print(response.content)
        text = json.loads(response.text)
        assert_text = text['msg']
        self.assertEqual(assert_text, data['assert'])
        time_intf = response.elapsed.total_seconds() * 1000
        time_intf = '%.2f' % time_intf
        print('接口耗时' + str(time_intf) + 'ms')
        print('预期结果：' + data['assert'] + '；实际结果：' + assert_text)
        print('The testcase was finished：' + data['ID'] + data['接口名称'])

    @ddt.data(*registerdata)
    def test_register(self, data):
        """人人说前端用户注册测试"""
        rq_method = data['method']
        url = data['url']
        if data['params']:
            params = json.loads(data['params'])
        else:
            params = ''
        headers = json.loads(data['headers'])
        response = requests.request(rq_method, url, headers=headers, params=params)
        if response.status_code != 200:
            print(response.content)
        text = json.loads(response.text)
        assert_text = text['msg']
        self.assertEqual(assert_text, data['assert'])
        time_intf = response.elapsed.total_seconds() * 1000
        time_intf = '%.2f' % time_intf
        print('接口耗时' + str(time_intf) + 'ms')
        print('预期结果：' + data['assert'] + '；实际结果：' + assert_text)
        print('The testcase was finished：' + data['ID'] + data['接口名称'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
