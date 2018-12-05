import requests
import base64
import utils

# 登录成功
url = "http://139.199.132.220:9000/event/api/register/"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
password = b"123huicehuice!@#"
data = {"username": "huice", "password": base64.b64encode(password)}
res = requests.post(url=url, headers=headers, data=data)
print(res.status_code)
print(res.json(), type(res))
token = res.json()["token"]
print(token)

# 添加会议
url = "http://139.199.132.220:9000/event/api/add_event/"
headers = {"Content-Type": "application/x-www-form-urlencoded", "Cookie": "token=" + token + ";uid=1"}
data = {"title": "huice接口测试沙龙1", "address": "北京", "time": "2018-11-30 10:00:00"}
sign = utils.ge_sign(token=token, params=data)
data["sign"] = sign
res = requests.post(url=url, headers=headers, data=data)
print(res.status_code)
print(res.text)
