import requests
import unittest
import jsonpath
import utils
from hit import *


class TestLogin(unittest.TestCase):
    """登录测试用例集合"""

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/register/"
        self.method = Method.POST
        self.datatype = Type.URL_ENCODED

    def test_login_success(self):
        """登录成功"""
        data = {"username": "fqivy", "password": utils.base64_encode("123123456")}
        # res = requests.post(url=self.url, data=data, headers=self.headers)
        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(res.json().get("error_code"), 0)
        # self.assertLess(res.elapsed.total_seconds(), 500)

        success_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        success_client.set_data(data=data)
        success_client.send()
        success_client.check_status_code(200)
        success_client.check_res_time_less(300)
        success_client.check_data_equal(success_client.res_json.get("error_code"), 10)

    def test_login_username_null(self):
        """用户名为空"""
        url = "http://127.0.0.1:8000/api/register/"
        data = {"username": "", "password": utils.base64_encode("123admin")}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("error_code"), 10001)
        self.assertLess(res.elapsed.total_seconds(), 500)

    def test_login_password_null(self):
        """密码为空"""
        url = "http://127.0.0.1:8000/api/register/"
        data = {"username": "fqivy", "password": ""}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("error_code"), 10001)
        self.assertLess(res.elapsed.total_seconds(), 500)

if __name__ == '__main__':
    unittest.main()
