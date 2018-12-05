import hashlib
import base64
import time
import assertpy


def ge_sign(token, params):
    """对传入的token和参数，生成sign"""
    params_list = []
    for key, value in params.items():
        if key != "sign":
            params_list.append(key + "=" + value)
    params_list.sort()
    print(params_list)
    res = "%spara=%s" % (token, "&".join(params_list))
    print(res)
    md5_sign = hashlib.md5()
    md5_sign.update(res.encode(encoding="utf-8"))
    sign = md5_sign.hexdigest()

    return sign


def base64_encode(string):
    """对传入的字符串进行base64转码"""
    string = bytes(string, encoding="utf-8")
    return base64.standard_b64encode(string)


def transform_mseconds(seconds):
    """将传入的秒值转化为整数毫秒值"""
    return int(round(seconds))


def ge_strf_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 60 * 60 * 48))
