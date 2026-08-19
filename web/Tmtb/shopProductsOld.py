#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/5/10 15:34
# @Author : Carey
# @File : shopProductsOld.py
# @Description
import re
from lxml import etree
import requests
from fontTools.ttLib import TTFont
import time


def getTruePrice( strEncPrice ):
    """
    字体反爬
    """
    path = 'assets/AlibabaSans102CustomFont.woff'
    base_font = TTFont(path)
    map_list = base_font.getBestCmap()

    en2num = {
        'period': ".",
        'two': '2',
        'zero': '0',
        'five': '5',
        'nine': "9",
        'seven': '7',
        'one': '1',
        'three': '3',
        'six': '6',
        'four': '4',
        'eight': '8'
    }

    for key in map_list.keys():
        if 0 == key or 'NULL' == map_list[key]:
            continue

        if map_list[key] not in en2num.keys():
            continue

        map_list[key] = en2num[map_list[key]]


    for key, value in map_list.items():
        strEncPrice = strEncPrice.replace('&#' + str(key) + ';', value)


    return strEncPrice


headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'bx-v': '2.5.11',
    'referer': 'https://zhoubaizi.taobao.com/category.htm?spm=a1z10.1-c.w4010-14261184496.2.5fa46010nq3Su5&search=y',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]

cookies ={
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': 'ce133f95aa9fe77f7aa62a5d6c655157_1728880605134',
    '_m_h5_tk_enc': 'fc95e3843655717cb69b3b41dc9b46ce',
    'cna': ETag,
    "_samesite_flag_": "true",
    '_tb_token_': 'e3107b3735eeb',
    'mtop_partitioned_detect': '1',
    "cookie2": "1db781de4526e70d95950d994895ea59",
}

response = requests.get(
    'https://caizhiqifs.tmall.com/i/asynSearch.htm?_ksTS=1715331892245_126&callback=jsonp338&input_charset=gbk&mid=w-22531731405-0&wid=22531731405&path=/search.htm&spm=a1z10.1-c.w4010-14261184496.2.5fa46010nq3Su5&search=y&pageNo=1',
    headers=headers,
    cookies=cookies
)
strHtml = re.findall( r"jsonp338\(\"(.*?)\"\)", response.text.strip(), re.S )

strTransToHtml = re.sub( r'\\"', '"', strHtml[0] )

html_text = etree.HTML( strTransToHtml )
wappers = html_text.xpath( './/div[@class="item3line1"] | .//div[@class="item5line1"]' )


products = []
for wapper in wappers:

    list = wapper.xpath( './/dl' )
    for item in list:
        info = {}

        info[ 'id' ]    = item.xpath('.//@data-id')[0].strip()
        url = item.xpath('.//dt[@class="photo"]/a[@class="J_TGoldData"]/@href')[0].strip()
        info[ 'url' ]   = f"https:{url}"


        lazyThumb = item.xpath('.//dt[@class="photo"]/a[@class="J_TGoldData"]/img/@data-ks-lazyload')
        if lazyThumb and lazyThumb[0] and len( lazyThumb[0] ) > 0:
            iLast = lazyThumb[0].rfind( '_' )
            thumb = lazyThumb[0][:iLast]
        else:
            thumb = item.xpath('.//dt[@class="photo"]/a[@class="J_TGoldData"]/img/@src')[0].strip()
        info[ 'thumb' ] = thumb

        info[ 'name' ] = item.xpath('.//dd[@class="detail"]/a[@class="item-name J_TGoldData"]/text()')[0].strip()
        priceNode = item.xpath('.//dd[@class="detail"]/div[@class="attribute"]/div[@class="cprice-area"]')
        strPriceHtml = str( etree.tostring( priceNode[0] ) )
        strEncPrice = re.findall( r'<span(?:\s+)class="c-price"(?:.*?)>(.*?)</span>', strPriceHtml, re.S )
        info[ 'price' ] = float( getTruePrice( strEncPrice[0].strip() ) )

        sale = item.xpath('.//dd[@class="detail"]/div[@class="attribute"]/div[@class="sale-area"]/span[@class="sale-num"]/text()')[0]
        info[ 'sale' ] = sale.strip()

        products.append( info )



print( len(products) )
for pinfo in products:
    print( pinfo )