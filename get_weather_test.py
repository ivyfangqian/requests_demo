import requests
import json

# get请求，url拼接参数
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset?theRegionCode=3117"
# res = requests.get(url)
# print(res.status_code)
# print(res.text)

# get请求，params参数传参
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset"
# params = {"theRegionCode": "3117"}
# res = requests.get(url, params=params)
# print(res.status_code)
# print(res.text)

# post请求,x-www-form-urlencoded，data参数为dict
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset"
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# data = {"theRegionCode": "3117"}
# res = requests.post(url=url, headers=headers, data=data)
# print(res.status_code)
# print(res.text)

# post请求，传xml参数
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx"
# headers = {"Content-Type": "text/xml; charset=utf-8"}
# data = """<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityDataset xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3117</theRegionCode>
#     </getSupportCityDataset>
#   </soap:Body>
# </soap:Envelope>"""
# res = requests.post(url=url, headers=headers, data=data)
# print(res.status_code)
# print(res.text)

# post请求，传json数据
# url = "http://139.199.132.220:9000/event/weather/getWeather/"
# headers = {"Content-Type": "application/json"}
# data = {"theCityCode": 1}
# res = requests.post(url=url, headers=headers, data=json.dumps(data))
# print(res.status_code)
# print(res.text)

# post请求，传json数据，方法二
# url = "http://139.199.132.220:9000/event/weather/getWeather/"
# headers = {"Content-Type": "application/json"}
# data = {"theCityCode": 1}
# res = requests.post(url=url, headers=headers, json=data)
# print(res.status_code)
# print(res.text)
# print(res.elapsed)

# 上传文件
# url = "http://139.199.132.220:9000/event/index/uploadFile/"
# res = requests.post(url=url, files={"myfile": open(r"d:\apk\logcat.txt", "rb")})
# print(res.status_code)
# print(res.text)


# 下载文件
# url = "http://139.199.132.220:9000/event/index/export/"
# res = requests.get(url)
# with open(r"./download.csv", "wb") as fb:
#     for i in res.iter_content(128):
#         fb.write(i)

# 设定超时时间
# url = "http://139.199.132.220:9001"
# res = requests.get(url, timeout=2)
# print(res.text)


# 持续时间
# url = "http://139.199.132.220:9000"
# res = requests.get(url)
# print(round(res.elapsed.total_seconds() * 1000))


# 解析xml
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3117"
# res = requests.get(url)
# print(res.status_code)
# print(res.text)
#
# # 使用ElementTree模块解析xml
# from xml.etree import ElementTree as ET
# # ET.parse("./xxx.xml")
# # findall获取所有符合元素,返回一个列表
# print(ET.fromstring(res.text).findall(".//{http://WebXml.com.cn/}string"))
# # find获取第一个符合元素，返回一个元素
# print(ET.fromstring(res.text).find(".//{http://WebXml.com.cn/}string").text)
#
# url = "http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset?theRegionCode=3117"
# res = requests.get(url)
# print(res.status_code)
# print(res.text)
# print(len(ET.fromstring(res.text).findall(".//CityID")))
# print(ET.fromstring(res.text).findall(".//CityID"))
# print(ET.fromstring(res.text).find(".//CityID").text)


# 解析json
url = "http://139.199.132.220:9000/event/weather/getWeather/"
headers = {"Content-Type": "application/json"}
data = {"theCityCode": 1}
res = requests.post(url=url, headers=headers, data=json.dumps(data))
print(res.status_code)
print(res.text)

# 解析json字符串，jsonpath.jsonpath(json对象，json解析格式)
import jsonpath

print(jsonpath.jsonpath(res.json(), "$.date"))
