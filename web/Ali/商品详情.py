#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/5/13 10:13
# @Author : Carey
# @File : 商品详情.py
# @Description
import json
import re

import requests
import  time
import hashlib


iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]


cookies ={
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': 'xxxxxxxxxxxxxxxx_xxxxxxxx',
    '_m_h5_tk_enc': 'xxxxxxxxxxxxxxxx',
    'cna': ETag,
    'x5sec':'7b22733b32223a2236353165643538383231633835313533222c226c61707574613b32223a226237353039346162303563616663356162343164653536656432323438363338434c766d2b724947454c37716d6558362f2f2f2f2f774577397179704b673d3d227d'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en',
    'Referer': 'https://www.1688.com/',
    'Host': 'detail.1688.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get( 'https://detail.1688.com/offer/853588602331.html?_t=1717481738143&spm=a2615.7691456.co_0_0_wangpu_score_0_0_0_0_0_0_0000_1.0', cookies=cookies, headers=headers )

storeData = re.findall( r"window\.__STORE_DATA=\{(.*?)<\/script>", response.text.strip(), re.S )
rJsonStore = json.loads( '{' + storeData[0] )
print(
    rJsonStore[ 'globalData' ][ 'sellerLoginId' ],
    str( rJsonStore[ 'components' ][ '38229149' ][ 'componentId' ] ) + '-' + rJsonStore[ 'components' ][ '38229149' ][ 'moduleData' ][ 'companyName' ],
    rJsonStore[ 'components' ][ '38229148' ][ 'moduleData' ][ 'companyName' ] + '-' + rJsonStore[ 'components' ][ '38229148' ][ 'moduleData' ][ 'detailAddress' ] ,
    rJsonStore[ 'globalData' ][ 'domain' ],
    rJsonStore[ 'globalData' ][ 'memberId' ],
)

productData = re.findall( r'window\.__INIT_DATA={(.*?)<\/script>', response.text.strip(), re.S )
rJsonProduct = json.loads( '{' + productData[0] )
print(  rJsonProduct['globalData'][ 'tempModel' ][ 'offerTitle' ] )


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
}

response = requests.get('https://itemcdn.tmall.com/1688offer/icoss25930840036434131ebaf3a393', headers=headers)

print( response )
print( response.text )
