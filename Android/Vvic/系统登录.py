#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/10/25 13:55
# @Author : Carey
# @File : 系统登录.py
# @Description
import time
import requests
from urllib.parse import urlparse
import hashlib



# acc = '18700477317'
# pasd = 'LEIjian0326'

acc = 'brandom@vip.qq.com'
pasd = 'sn5diphone6'

headers = {
    'andriodid': '12e7b43fb83ffc1e',
    'os': '2',
    'app-version': '4.52.0',
    'api-sign': '2719a33c9b9924de374b0926d7d69e7d',
    'Content-Type': 'application/x-www-form-urlencoded',
    'device-id': 'b92e4793525b23ce4d05838a2ef05bca',
    'device-token': 'AoUwqRYh6BnATd-pgljnm6AvPlcKrl_Ry3YVcdYqxDa1',
    'device-ua': 'Mozilla/5.0 (Linux; Android 9; G576D Build/PQ3A.190605.09291615; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36',
    'User-Agent': 'Vvic/4.93.0 (Google+Phone+G576D; Android 9)',
}


url = 'https://app.vvic.com/v1/login'

urlInfo = urlparse( url )

data = {
    'password': pasd,
    'username': acc,
    'nonce_str': 'ovwmhhtmgw',
    'timeStamp': int( time.time() * 1000 )
}

strData = ''
for key,item in data.items():
    strData += f"{key}={item}&"


strEnc = f"{urlInfo.path}{strData.strip('&')}d1=-d=-aingia=="
sign = hashlib.md5( strEnc.encode(encoding='UTF-8')).hexdigest()

headers[ 'api-sign' ] = sign
response = requests.post( url, data=data, headers=headers )

print( response.status_code )
print( response.text )

print( response.json()[ 'data' ][ 'user_id' ] )
print( response.json()[ 'data' ][ 'nickname' ] )
print( response.json()[ 'data' ][ 'email' ] )
print( response.json()[ 'data' ][ 'token' ] )