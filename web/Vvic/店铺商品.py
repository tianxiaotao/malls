#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/5/20 15:20
# @Author : Carey
# @File : shopProductsOld.py
# @Description
import requests


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Cookie': 'source=m;userLoginAuto=1;vvic_token=xxxxxxxx-2d0e-43f7-978a-xxxxxxxxx;userName=vvic9150080000;umc=1;pn=0;',
    'Referer': 'https://www.vvic.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'token': '',
}

params = {
    'id': '79157',
    'currentPage': '1',
    'sort': 'up_time-desc',
    'merge': '0',
}

response = requests.get( 'https://www.vvic.com/apif/shop/itemlist', params=params, headers=headers )
print( response )
print( response.text )
