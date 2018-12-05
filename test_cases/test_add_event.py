import requests
import unittest
import jsonpath
import utils
import time


class TestAddEvent(unittest.TestCase):
    """添加会议测试用例集合"""

    def test_add_event_success(self):
        """添加会议成功"""
        url = "http://127.0.0.1:8000/api/add_event/"
        data = {"title": "互联网测试技术大会" + str(time.time()),
                "address": "北京国家会议中心",
                "time": utils.ge_strf_time()}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("error_code"), 0)
        self.assertLess(res.elapsed.total_seconds(), 500)

    def test_add_event_title_null(self):
        """标题为空"""
        url = "http://127.0.0.1:8000/api/add_event/"
        data = {"title": "",
                "address": "北京国家会议中心",
                "time": utils.ge_strf_time()}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("error_code"), 10001)
        self.assertLess(res.elapsed.total_seconds(), 500)

    def test_add_event_address_null(self):
        """地址为空"""
        url = "http://127.0.0.1:8000/api/add_event/"
        data = {"title": "互联网测试技术大会" + str(time.time()),
                "address": "",
                "time": utils.ge_strf_time()}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("error_code"), 10001)
        self.assertLess(res.elapsed.total_seconds(), 500)


if __name__ == '__main__':
    unittest.main()
