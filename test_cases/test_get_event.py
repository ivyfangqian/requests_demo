from hit_asserpy import *

client = Client("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3113",
                method=Method.GET)
client.send()
print(client.res_text)
client.check_status_code(300)

# 判断是否是回文字符串
string = "madam"


def is_palindromic(string=None):
    if isinstance(string, str):
        # 标识初始值为True
        flag = True

        if string != string[::-1]:
            flag = False
        return flag
    else:
        raise TypeError("输入不是字符串")


# 把字典{"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}，变为{'a': 'aa', 'b': 'bb', 'd': 'dd', 'e': 'ee'}格式。

dict1 = {"a": "aa", "b": "bb", "c": {"d": "dd", "e": "ee"}}
res = {}
for k, v in dict1.items():
    if isinstance(v, str):
        res[k] = v
    else:
        for kk, vv in v.items():
            res[kk] = vv
print(res)
