#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description

import json
from urllib3.exceptions import InsecureRequestWarning
import requests
import time
import execjs
import urllib.parse
import base64
import re
import sys



def execJsFile( file = './assets/world_search.js' ):
    """
    执行JS预编译
    """
    with open( file, "r", encoding='utf-8') as f:
        js_tamp = f.read()
    jsDrive = execjs.compile(js_tamp)

    return jsDrive


iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]

strCookie = f'cna={ETag}; cookie2=11aaeb645c689ca1015417a31c772057; mtop_partitioned_detect=1; _samesite_flag_=true; cancelledSubSites=empty; sgcookie=E100pwEUrhK5vMidcMGFoByUEyFjs5meKMMSrTsY6YhzqWvNGk%2B82vb%2FAZAfdhx1lHK6qcqY2fCQJ8rFRCeIYYcu4%2BuH3Rs66YPAMABvjbQHGENTjwHI4tqiULf4iMvrNnsP; csg=99a61954; _l_g_=Ug%3D%3D; sg=423; _m_h5_tk=d93d342c886cd3db7bcfeb005a3a9cc1_1746010214768; _m_h5_tk_enc=128e8d6a31321ee91a6b4dad1c429e12; havana_lgc2_0=eyJoaWQiOjg3NDU1MjIzMiwic2ciOiI3Zjk0YTNhOGQ0MmQxMzkyMjY4MmM5MWY5ZmRlM2U1OCIsInNpdGUiOjAsInRva2VuIjoiMUhNTlFZNEY3TmZJUGl5WTR4XzRFUUEifQ'


'''
提取cookie中 _m_h5_tk 的值
'''
token = re.findall( r'_m_h5_tk=(.*?)_(?:.*?);', strCookie )
if False == token or len(token[0]) <= 0:
    print( '当前cookie无效， 未识别出来【_m_h5_tk】值' )
    sys.exit()

img = './assets/abc.jpg'
with open(img, "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read())

strImg = encoded_string.decode()

params = {
    "pcGraphSearch": 'true',
    "region": "",
    "strimg": strImg,
    "sortOrder": "0",
    "ttid": "600000@taobao_android_10.16.10",
    "tab": "all",
    "sversion": 15.8,
    "vm": "nw",
}

data = {
    "appId": "34850",
    "params": json.dumps(params, ensure_ascii=False).replace(' ', '')
}

t = int(time.time() * 1000)
c = json.dumps(data, ensure_ascii=False).replace(' ', '')

jsDrive = execJsFile( 'assets/world_search.js' )
sign = jsDrive.call('getSign', token, t, c)

config = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": t,
    "sign": sign,
    "api": "mtop.relationrecommend.WirelessRecommend.recommend",
    "v": "2.0",
    "type": "originaljson",
    "isSec": 1,
    "dataType": "jsonp"
}
query = urllib.parse.urlencode(config)
url = f'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?{query}'

headers = {
    "Accept": "application/json",
    "Accept-Language": "en",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://world.taobao.com",
    "Referer": "https://world.taobao.com/",
    "Cookie": strCookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

timeout = 120
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.post(url=url, data={"data": c}, headers=headers, timeout=timeout, verify=False)
print( response.cookies.get_dict() )

if 200 == response.status_code:
    respInfo = response.json()

    if respInfo['data'].get('itemsArray'):
        print(respInfo['data']['itemsArray'])
    elif respInfo['data'].get('pcGraphNavModule'):
        if respInfo['data']['pcGraphNavModule'].get('itemsArray'):
            print(respInfo['data']['pcGraphNavModule']['itemsArray'])
        else:
            print(respInfo)
    else:
        print(respInfo)
else:
    print(response.status_code)
