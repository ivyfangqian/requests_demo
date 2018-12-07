from hit import *
import unittest
import time
import utils


class AddEventTest(unittest.TestCase):
    """添加会议接口测试集"""

    def setUp(self):
        self.url = "http://139.199.132.220:9000/event/api/add_event/"
        self.method = Method.POST
        self.datatype = Type.URL_ENCODED
        self.token = Client.get_env_param("token")
        self.uid = Client.get_env_param("uid")

    def test_add_event_success(self):
        """添加会议成功"""
        add_event_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        self.data = {"title": "互联网测试技术大会" + str(time.time()),
                     "address": "北京国家会议中心",
                     "time": utils.ge_strf_time()}
        add_event_client.add_header("Cookie", "token=%s;uid=%s" % (self.token, self.uid))
        add_event_client.set_data(self.data)
        add_event_client.add_sign(self.token)
        add_event_client.send()
        add_event_client.check_status_code(200)
        add_event_client.check_res_time_less(200)
        add_event_client.check_data_equal(add_event_client.res_json.get("error_code"), 0)

    def test_add_event_title_null(self):
        """添加会议标题为空"""
        add_event_client = Client(url=self.url, method=self.method, datatype=self.datatype)
        self.data = {"title": "",
                     "address": "北京国家会议中心",
                     "time": utils.ge_strf_time()}
        add_event_client.add_header("Cookie", "token=%s;uid=%s" % (self.token, self.uid))
        add_event_client.set_data(self.data)
        add_event_client.add_sign(self.token)
        add_event_client.send()
        add_event_client.check_status_code(200)
        add_event_client.check_res_time_less(200)
        add_event_client.check_data_equal(add_event_client.res_json.get("error_code"), 10001)
