#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/4/11 16:52
# @Author : Carey
# @File : shopProductsOld.py
# @Description
import json
import re
import requests
import  time
import hashlib

iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]


cookies = {
    '_m_h5_tk': 'xxxxxxxxxxxxxxxx_xxxxxxxx',
    '_m_h5_tk_enc': 'xxxxxxxxxxxxxxxx',
    'cna': ETag,
    'mtop_partitioned_detect': '1',
    'x5sec':'7b22733b32223a2236353165643538383231633835313533222c226c61707574613b32223a226237353039346162303563616663356162343164653536656432323438363338434c766d2b724947454c37716d6558362f2f2f2f2f774577397179704b673d3d227d'
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://detail.1688.com',
    'Referer': 'https://detail.1688.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


arg = {
    'appName': 'pcmodules',
    'resourceName': 'wpOfferColumn',
    'memberId': 'b2b-2616586436520f7',
    'type': 'view',
    'version': '1.0.0',
    'appdata':  {
        'sortType': 'wangpu_score',
        'sellerRecommendFilter': 'false',
        'mixFilter': 'false',
        'tradenumFilter': 'false',
        'quantityBegin': 'null',
        'pageNum': 1,
        'count': 30,
    }
}
data = {
    'dataType': 'moduleData',
    'argString': json.dumps( arg, ensure_ascii=False).replace(' ', '')
}

postData = {
    "data": json.dumps( data,  ensure_ascii=False ).replace(' ', ''),
}

strTime = str( round( time.time()*1000 ) )
params = {
    'jsv': '2.4.11',
    'appKey': '12574478',
    't': strTime,
    'api': 'mtop.1688.shop.data.get',
    'v': '1.0',
    'type': 'json',
    'valueType': 'string',
    'dataType': 'json',
    'timeout': '10000',
}
strEnc = cookies['_m_h5_tk'].split('_')[0] + "&" + strTime +  "&" +  params['appKey'] + "&" + postData['data']

sign = hashlib.md5( strEnc.encode(encoding='UTF-8')).hexdigest()
params[ 'sign' ] = sign

response = requests.post( 'https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/', params=params, cookies=cookies, headers=headers, data=postData )

list = response.json()[ 'data' ][ 'content' ][ 'offerList' ]
print( len( list ) )
for item in list:
    info = {
        'id': item[ 'id' ],
        'title': item[ 'subject' ],
        'created': item[ 'gmtCreate' ],
        'images': item['offerImages'],
        'collects': item['bookedCount'],
        'memberId': item['memberId'],
        'price': item[ 'price' ],
        'min_price': item[ 'underLinePrice' ],
        'sales': item['ninetySaleQuantity'],
        'status': item[ 'status' ]
    }
    if 'mainVideoId' in item:
        info[ 'video' ] = item['mainVideoId']

    print( info )
