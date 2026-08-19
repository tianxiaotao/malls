#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description
import os

from PIL import Image
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

strCookie = f'cna={ETag}; cookie2=1f92903dab781908801b38840ff9339b; mtop_partitioned_detect=1; _samesite_flag_=true; cancelledSubSites=empty; wk_unb=W875Pb56bzoW; _l_g_=Ug%3D%3D; sg=423;  _m_h5_tk=e75874a32abd88c6eb41515c0e2c2c87_1746012195607; _m_h5_tk_enc=8ac53a0db4c39932c1f295029fea76ae; havana_lgc2_0=eyJoaWQiOjg3NDU1MjIzMiwic2ciOiI3Zjk0YTNhOGQ0MmQxMzkyMjY4MmM5MWY5ZmRlM2U1OCIsInNpdGUiOjAsInRva2VuIjoiMUhNTlFZNEY3TmZJUGl5WTR4XzRFUUEifQ'


'''
提取cookie中 _m_h5_tk 的值
'''
token = re.findall( r'_m_h5_tk=(.*?)_(?:.*?);', strCookie )
if False == token or len(token[0]) <= 0:
    print( '当前cookie无效， 未识别出来【_m_h5_tk】值' )
    sys.exit()

img = './assets/abc.jpg'
def compress_image(image_path, target_size):
    image = Image.open(image_path)
    image.thumbnail(target_size)
    image.save('./assets/compressed_image.jpg')  # 保存压缩后的图片
    return './assets/compressed_image.jpg'

image_path = img
target_size = (800, 600)  # 目标尺寸
fname = compress_image(image_path, target_size)

with open( fname, "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read())

strImg = encoded_string.decode( 'utf-8' )

jsRadomDrive = execJsFile( './assets/random.js' )
random = jsRadomDrive.call( 'getRandom' )

jsPicSignDrive = execJsFile( './assets/sha256.js' )
param = {
    'pageFrom': 'a21n57.imgsearch',
    'imgFrom': 'upload',
    'random': random,
    'timestamp':str( iTime )
}
strParam = json.dumps( param, ensure_ascii=False).replace(' ', '')
picSign = jsPicSignDrive.call( 'getPicSign', strParam + '6dbd0668a0634ae9badd25d3da236f47' )

param[ 'page' ] = 1
param[ 'pageSize' ] = 60
param[ 'strimg' ] = strImg
param[ 'ttid' ] = '1@tbwang_mac_1.0.0#pc'
param[ 'pcSign' ] = picSign

data = {
    'appId': 46006,
    'params': json.dumps( param, ensure_ascii=False).replace(' ', '')
}

c = json.dumps(data, ensure_ascii=False).replace(' ', '')

jsDrive = execJsFile( './assets/world_search.js' )
sign = jsDrive.call('getSign', token, iTime, c)

config = {
    'jsv': '2.7.4',
    'appKey': '12574478',
    't': iTime,
    'sign': sign,
    'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
    'v': '2.0',
    'type': 'originaljson',
    'dataType': 'jsonp'
}
query = urllib.parse.urlencode(config)
url = f'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?{query}'

headers = {
    "Accept": "application/json",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://s.taobao.com",
    "Referer": "https://s.taobao.com/",
    "Cookie": strCookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

response = requests.post(url=url, data={"data": c}, headers=headers)
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
