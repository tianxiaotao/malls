#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/6/3 17:30
# @Author : Carey
# @File : 店铺商品.py
# @Description
import time
import json
import requests
import execjs
import re
import sys



iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]

strCookie = f'wk_unb=W875Pb56bzoW; cookie2=11aaeb645c689ca1015417a31c772057; cna={ETag}; cancelledSubSites=empty; xlly_s=1; mtop_partitioned_detect=1; _samesite_flag_=true; sgcookie=E100yY9lrn581FInbq558f0Le6WKch8CW0l9oXBjRM6c0Q%2FiJdXT03pAPzZVJvGNSBrsWbsBIEDTQ0%2BgCpV5R%2FFbIxglXuHLKnNp05YjPO6ab3b6p9RMAzYSjSAqkrOLRRFF; csg=99a61954; _l_g_=Ug%3D%3D; sg=423; _m_h5_tk=9009c4b8d0f8b63b78c4330c1f7aedf2_1729774552138; _m_h5_tk_enc=c98f12b1fdf287412446c05f3d6c2dcf'


'''
提取cookie中 _m_h5_tk 的值
'''
token = re.findall( r'_m_h5_tk=(.*?)_(?:.*?);', strCookie )
if False == token or len(token[0]) <= 0:
    print( '当前cookie无效， 未识别出来【_m_h5_tk】值' )
    sys.exit()


headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.taobao.com',
    'Referer': 'https://www.taobao.com/',
    'Cookie': strCookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

def execJsFile( file = 'detail.js' ):
    """
    执行JS预编译
    """
    with open( file, "r", encoding='utf-8') as f:
        js_tamp = f.read()
    jsDrive = execjs.compile(js_tamp)

    return jsDrive


data = {
    'shopId': '523256652',
    'sellerId': '2854916506',
    'page': 2,
    'orderType': 'first_new',  # first_new 时间； popular 综合； uvsum365 销量；  inshop_discount_price【asc/des】 价格正倒序
    'sortType': '',
    'catId': 0,
    'keyword':'',
    'filterType': ''
}
rtime = round( time.time() * 1000)
c = json.dumps(data).replace(' ', '')

jsDrive = execJsFile('assets/detail.js')
sign = jsDrive.call('_getSign', token[0], rtime, c)

params = {
    'jsv': '2.6.2',
    'appKey': '12574478',
    't': str(rtime),
    'sign': sign,
    'api': 'mtop.taobao.shop.simple.item.fetch',
    'type': 'originaljson',
    'v': '1.0',
    'timeout': '10000',
    'dataType': 'json',
    'sessionOption': 'AutoLoginAndManualLogin',
    'needLogin': 'true',
    'LoginRequest': 'true',
    'jsonpIncPrefix': f'_{str(rtime)}_',
    'data': json.dumps( data, ensure_ascii=False).replace(' ', ''),
}

response = requests.get( 'https://h5api.m.taobao.com/h5/mtop.taobao.shop.simple.item.fetch/1.0/', params=params, headers=headers )
print( response.cookies.get_dict() )
print( response.json()['data']['url'] )




print(  f"{response.json()[ 'data' ][ 'totalCnt' ]} ---> {len( response.json()[ 'data' ][ 'data' ]  )}"  )
print( response.json()[ 'data' ]['data'] )