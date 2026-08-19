#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/11 15:18
# @Author : Carey
# @Description

import json
import re
import sys
import requests
import time
import execjs
from urllib.parse import urlparse



iTime = round( time.time() * 1000 )
response = requests.get( f'https://log.mmstat.com/eg.js?t={iTime}'  )
ETag = re.findall( r'goldlog.Etag="(.*?)";', response.text.strip() )[0]


strCookie = f'cna={ETag}; cancelledSubSites=empty; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=e75874a32abd88c6eb41515c0e2c2c87_1746012195607; _m_h5_tk_enc=8ac53a0db4c39932c1f295029fea76ae; _samesite_flag_=true; cookie2=1f92903dab781908801b38840ff9339b; sg=423'

'''
提取cookie中 _m_h5_tk 的值
'''
token = re.findall( r'_m_h5_tk=(.*?)_(?:.*?);', strCookie )
if False == token or len(token[0]) <= 0:
    print( '当前cookie无效， 未识别出来【_m_h5_tk】值' )
    sys.exit()

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': strCookie,
    'Origin': 'https://detail.taobao.com',
    'Referer': 'https://detail.taobao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


'''
解析url链接 为sign生成做准备值
'''
url = 'https://item.taobao.com/item.htm?abbucket=16&id=736398693388&ns=1&priceTId=2150443f17298212003856469ef353&skuId=5257036278349&spm=a21n57.1.item.95.4898523cTQUmtw&utparam=%7B%22aplus_abtest%22%3A%22e5d89d190bb0d94e51531005f2cd15a2%22%7D&xxc=taobaoSearch'

#url = 'https://detail.tmall.com/item.htm?id=702776403900&spm=a21bo.jianhua/a.201876.d3.5af92a89KWxkl9&scm=1007.40986.387801.0&pvid=d9f75829-1fc6-432c-9698-badfe3707e82&xxc=home_recommend&priceTId=2147818417223229550576166e9c36'
urlInfo = urlparse( url )

if False == urlInfo.query or len( urlInfo.query ) <= 0:
    sys.exit()

queryInfo = urlInfo.query.split( '&' )
arrParams = {}
for item in queryInfo:
    arrIt = item.split( '=' )
    if arrIt:
        arrParams.update({arrIt[0]:arrIt[1]})
    else:
        continue

exParams = {
    "queryParams": urlInfo.query,
    "domain": f"{urlInfo.scheme}//{urlInfo.netloc}",
    "path_name": urlInfo.path
}
for k in arrParams:
    if k in arrParams and len( arrParams[k] ) > 0:
        exParams.update({k: arrParams[k]})
    else:
        continue


def execJsFile( file = 'detail.js' ):
    """
    执行JS预编译
    """
    with open( file, "r", encoding='utf-8') as f:
        js_tamp = f.read()
    jsDrive = execjs.compile(js_tamp)

    return jsDrive


def getProductDetailInfo():
    """
    商品详细数据
    """
    '''
    构建请求参数
    '''
    data = {
        'id': arrParams['id'],
        'detail_v': '3.3.2',
        'exParams': json.dumps(exParams, ensure_ascii=False).replace(' ', '')
    }
    rtime = round(time.time() * 1000)
    c = json.dumps(data).replace(' ', '')

    jsDrive = execJsFile('assets/detail.js')
    sign = jsDrive.call('_getSign', token[0], rtime, c)

    params = {
        'jsv': '2.6.1',
        'appKey': '12574478',
        't': str(rtime),
        'sign': sign,
        'api': 'mtop.taobao.pcdetail.data.get',
        'v': '1.0',
        'isSec': '0',
        'ecode': '0',
        'timeout': '10000',
        'ttid': '2022@taobao_litepc_9.17.0',
        'AntiFlood': 'true',
        'AntiCreep': 'true',
        'dataType': 'json',
        'valueType': 'string',
        'preventFallback': 'true',
        'type': 'json',
        'data': json.dumps( data, ensure_ascii=False).replace(' ', ''),
    }
    '''
    发起请求 + 解析数据
    '''
    response = requests.get( 'https://h5api.m.taobao.com/h5/mtop.taobao.pcdetail.data.get/1.0/', params=params, headers=headers )
    print( response.cookies.get_dict() )

    coupon = None
    strCoupon = None
    if 'extensionInfoVO' in response.json()['data']['componentsVO']:
        couponInfo = response.json()[ 'data' ][ 'componentsVO' ][ 'extensionInfoVO' ]
        if couponInfo and len( couponInfo ) > 0:
            for row in couponInfo[ 'infos' ]:
                if 'DAILY_COUPON' != row[ 'type' ]:
                    continue

                strCoupon = f"{row['title']}：{row[ 'items' ][0][ 'text' ][0]}"
                arrCoupons =  re.findall( r'满(?:\d+)减(\d+)|抵((\d+)(\.\d+)?)', row[ 'items' ][0][ 'text' ][0], re.S )
                if len( arrCoupons ) > 0 and arrCoupons[0]:
                    if arrCoupons[0][1]:
                        coupon = arrCoupons[0][1]
                    if arrCoupons[0][0]:
                        coupon = arrCoupons[0][0]

    print( f'优惠信息：【{strCoupon}】 优惠金额：{coupon} ￥' )
    print( response.json()[ 'data' ][ 'componentsVO' ]['priceVO'] )


def getProoductDesrcInfo():
    """
    商品描述
    """
    data = {
        'id': arrParams['id'],
        'detail_v': '3.3.2',
        'preferWireless': 'true',
    }
    for key in arrParams:
        data[key] = arrParams[ key ]

    rtime = round( time.time() * 1000 )
    c = json.dumps(data).replace(' ', '')
    jsDrive = execJsFile('assets/detail.js')
    sign = jsDrive.call('_getSign', token[0], rtime, c)

    '''
    构建请求参数
    '''
    params = {
        'jsv': '2.7.2',
        'appKey': '12574478',
        't': str(rtime),
        'sign': sign,
        'api': 'mtop.taobao.detail.getdesc',
        'dangerouslySetWindvaneParams': '%5Bobject%20Object%5D',
        'v': '7.0',
        'isSec': '0',
        'ecode': '0',
        'timeout': '3000',
        'ttid': '2022@tmall_litepc_9.17.0',
        'type': 'jsonp',
        'AntiFlood': 'true',
        'AntiCreep': 'true',
        'H5Request': 'true',
        'dataType': 'jsonp',
        'valueType': 'jsonp',
        'callback': 'mtopjsonp1',
        'data': json.dumps(data, ensure_ascii=False).replace(' ', ''),
    }
    '''
    发起请求 + 解析数据
    '''
    headers[ 'Accept' ] = '*/*'
    del headers[ 'Accept-Encoding' ]

    response = requests.get('https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdesc/7.0/', params=params, headers=headers )
    data = re.findall( r"mtopjsonp(?:\d+)\((.*?)\)$", response.text.strip(), re.S )
    result = json.loads( data[0].strip() )
    for k,val in result[ 'data' ][ 'components' ][ 'componentData' ].items():
        if 'desc_richtext_pc' == k or re.match( r"^detail_rich_text_(\d)", k ):
            print( val[ 'model' ][ 'text' ] )

        if None == re.match( r"^detail_pic", k ):
            continue

        if True == val[ 'model' ][ 'picUrl' ].startswith( '//' ):
            val['model']['picUrl'] = f"https:{val[ 'model' ][ 'picUrl' ]}"
        print( val[ 'model' ][ 'picUrl' ] )


if __name__ == '__main__':
    #getProductDetailInfo()
    getProoductDesrcInfo()