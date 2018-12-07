import unittest
from hit import *
import utils


class LoginTest(unittest.TestCase):
    """登录接口测试集"""

    def setUp(self):
        self.url = "http://139.199.132.220:9000/event/api/register/"
        self.method = Method.POST
        self.datatype = Type.URL_ENCODED

    def test_login_success(self):
        """登录成功测试用例"""
        self.data = {"username": "huice", "password": utils.base64_encode("123huicehuice!@#")}
        login_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        login_client.set_data(self.data)
        login_client.send()
        login_client.check_status_code(200)
        login_client.check_res_time_less(200)
        login_client.check_data_equal(login_client.res_json.get("error_code"), 0)
        Client.save_evn_param("token", login_client.res_json.get("token"))
        Client.save_evn_param("uid", login_client.res_json.get("uid"))

    def test_login_username_null(self):
        """登录-- 用户名为空"""
        self.data = {"username": "", "password": utils.base64_encode("123huicehuice!@#")}
        login_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        login_client.set_data(self.data)
        login_client.send()
        login_client.check_status_code(200)
        login_client.check_res_time_less(200)
        login_client.check_data_equal(login_client.res_json.get("error_code"), 10001)

    def test_login_password_null(self):
        """登录-- 密码为空"""
        self.data = {"username": "huice", "password": ""}
        login_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        login_client.set_data(self.data)
        login_client.send()
        login_client.check_status_code(200)
        login_client.check_res_time_less(200)
        login_client.check_data_equal(login_client.res_json.get("error_code"), 10001)
