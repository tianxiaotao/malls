#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/10/24 10:48
# @Author : Carey
# @File : 店铺商品.py
# @Description
import requests


headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://shop.m.dangdang.com/',
    'Origin': 'http://shop.m.dangdang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

shopid = 8064
params = {
    'shop_id': shopid,
    'action': 'shop_search',
    'sort_type': 'default',  # default -默认，sale -销量，price -价格， rank -好评，time -最新
}
data = {
    'page_no': 1,
    'ajax': 1,
}

url = 'http://shop.m.dangdang.com/shop.php'
response = requests.post( url, params=params, data=data, headers=headers )

print( response.text )
