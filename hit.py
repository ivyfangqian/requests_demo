import requests
import unittest


class Client(unittest.TestCase):
    """Client(url, method, datatype=None)"""

    def __init__(self, url, method, datatype=None):
        self.__url = url
        self.__method = method
        self.__datatype = datatype
        self.__headers = {}
        self.__data = {}
        self.__res = None
        self._type_equality_funcs = {}

    def add_header(self, key, value):
        """添加头信息"""
        self.__headers[key] = value

    def set_data(self, data):
        """添加接口参数"""
        self.__data = data

    def send(self):
        """根据发送数据方式，发送数据"""

        # 发送GET请求
        if self.__method == "GET":
            self.__res = requests.get(url=self.__url, params=self.__data)
        # 发送POST请求
        elif self.__method == "POST":
            # 发送普通form-data
            if self.__datatype == 0:
                self.__res = requests.post(url=self.__url, data=self.__data)
            # 发送x-www-url-form-url-encoded数据
            elif self.__datatype == 1:
                self.add_header("Content-Type", "application/x-www-form-urlencoded")
                self.__res = requests.post(url=self.__url, data=self.__data, headers=self.__headers)
            # 发送json数据
            elif self.__datatype == 2:
                self.add_header("Content-Type", "application/json")
                self.__res = requests.post(url=self.__url, json=self.__data, headers=self.__headers)
            # 发送xml格式数据
            elif self.__datatype == 3:
                xml = self.__data["xml"]
                if xml:
                    self.add_header("Content-Type", "text/xml")
                    requests.post(url=self.__url, data=self.__data, headers=self.__headers)
                else:
                    raise Exception('xml数据传输错误，请按照{"xml":"xxxx"}方式进行传输')
            else:
                raise Exception("请求类型不合法")
        else:
            raise Exception("不支持的请求方法类型")

    @property
    def res_text(self):
        """返回响应正文字符串"""
        if self.__res:
            return self.__res.text
        else:
            return None

    @property
    def res_status_code(self):
        """返回响应状态码"""
        if self.__res:
            return self.__res.status_code
        else:
            return None

    @property
    def res_json(self):
        """返回响应json对象"""
        if self.__res:
            try:
                return self.__res.json()
            except Exception:
                print("json数据转换失败")
                return None
        else:
            return None

    @property
    def res_time(self):
        """返回响应时间毫秒值"""
        if self.__res:
            return int(round(self.__res.elapsed.total_seconds()))
        else:
            return None

    @property
    def res_headers(self):
        if self.__res:
            return self.__res.headers
        else:
            return None

    def check_status_code(self, expect):
        """check_status_code(expect)，校验响应状态码"""
        self.assertEqual(self.res_status_code, expect)
        print("状态码校验成功：实际状态码[{actual}]，预期状态码[{expect}]".format(actual=self.res_status_code, expect=expect))

    def check_res_time_less(self, expect_time):
        """check_res_time_less(self, expect_time)，校验响应时间"""
        self.assertLess(self.res_time, expect_time)
        print("响应时间校验成功：实际响应时间[{actual}]，预期响应时间[{expect}]".format(actual=self.res_time, expect=expect_time))

    def check_data_equal(self, actual, expect):
        """check_data_equal(self,actual,expect)，校验响应内容"""
        self.assertEqual(actual, expect)
        print("响应内容校验成功：实际响应内容[{actual}]，预期响应内容[{expect}]".format(actual=actual, expect=expect))

    def check_contains(self, expect):
        """check_contains(self, expect)，校验响应正文是否包含内容"""
        self.assertIn(expect, self.res_text)
        print("响应内容包含校验成功：实际响应内容[{actual}]，预期包含内容[{expect}]".format(actual=self.res_text), expect=expect)


class Method(object):
    GET = "GET"
    POST = "POST"


class Type(object):
    FORM = 0
    URL_ENCODED = 1
    JSON = 2
    XML = 3
    FILE = 4
