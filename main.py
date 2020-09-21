#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
data = {"email":"admin@jixiaokang.com","password":"930315"}
url ='https://wheremylife.cn/1.0/user/login'
session = requests.Session()
session.post(url,headers = headers,data = data)
# 登录后，我们先打卡
response = session.post('https://wheremylife.cn/1.0/user/resetBook',headers = headers)
active = {
    "active": true,
    "hour": 0,
    "targetEmails": [
        "8618538715282_f0IpcJ@kindle.cn",
        "8618538715282@kindle.cn",
        "8618538715282_2710b6@kindle.cn"
    ],
    "type": "EVERY_3_DAYS"
}
res = session.post('https://wheremylife.cn/1.0/user/setNoti',headers = headers,data = active)
# 登录后，我们然后设置激活
print(response.status_code)
print(response.text)
print(res.text)
