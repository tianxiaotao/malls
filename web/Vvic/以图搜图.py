#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/7/17 17:13
# @Author : Carey
# @File : 以图搜图.py
# @Description
import random
from requests_toolbelt import MultipartEncoder
import requests
import string
import os


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Cookie': 'source=m;userLoginAuto=1;vvic_token=5129759f-1d9b-4815-8c34-88487e267db6;uid=2862702;userName=vvic9153980633;umc=1;pn=0',
    'Referer': 'https://tusou.vvic.com',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

arrProxy = [
    { 'host': 'http-dyn.abuyun.com', 'port': '9020', 'user': 'H3Y74E32U40W05WD', 'passwd':'2C28A7BADDEFC07E' },
    { 'host': 'http-dyn.abuyun.com', 'port': '9020', 'user': 'HF3EB2F5Z234U93D', 'passwd':'D4EF9422DB13799A' },
    # { 'host': 'http-proxy-t3.dobel.cn', 'port': '9180', 'user': 'BBBBBBAE8ITN4O0', 'passwd':'LBMEcBEa' },
    # { 'host': 'http-proxy-t3.dobel.cn', 'port': '9180', 'user': 'AAAAAA0EIITMO90', 'passwd':'2ckMpwue' },
]

proxy = random.choice( arrProxy )
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxy[ 'host' ],
    "port": proxy[ 'port' ],
    "user": proxy[ 'user' ],
    "pass": proxy[ 'passwd' ],
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

print( proxies )

def getOssPolicy():
    headers[ 'Content-Type' ] = 'application/x-www-form-urlencoded'
    response = requests.get('https://tusou.vvic.com/api/getOssPolicy', headers=headers, proxies=proxies )

    if 200 == response.status_code:
        return response.json()
    else:
        print( response.status_code )
    return False

def getRandomName( num = 10 ):
    str = string.ascii_letters + string.digits
    return "".join( random.sample( str, num ) )


def uploadImg( conf ):
    img = 'abc.png'
    imgSuffix = img.split( '.' )[-1]
    fkey = f"{conf[ 'dir' ]}{getRandomName()}.{imgSuffix}"

    headers['Accept'] = '*/*'
    enc = MultipartEncoder(
        fields={
            'key': fkey,
            'policy': conf['policy'],
            'name': f'{getRandomName()}.{imgSuffix}',
            'OSSAccessKeyId': conf['accessid'],
            'success_action_status': '200',
            'callback': conf['callback'],
            'signature': conf['signature'],
            'file': ( os.path.basename( img ), open( img, 'rb' ), 'image/jpeg' ),
        },
        boundary=f"----WebKitFormBoundary{getRandomName( 16 )}"
    )
    headers['Content-Type'] = enc.content_type
    response = requests.post( conf['host'], headers=headers, data=enc )
    response.encoding = 'utf-8'
    if response.status_code != 200:
        print( response.json() )
        return False

    return  f'{conf["host"]}/{fkey}'

def getSearchResult( imgUrl, page=1 ):
    url = f'https://tusou.vvic.com/api/uploadImage?url={imgUrl}&searchCity=gz'
    res = requests.get(url, headers=headers, proxies=proxies)
    if res.status_code != 200:
        print( res )
        return False

    params = {
        'sort': 'default',
        'isStrength': 0,
        'cityMarketCode': 'gz',
        'mergeSpam': 1,
        'panggeFlag': 0,
        'imgStr': None,
        'md5': res.json()[ 'appMd5' ],
        'scene': 7,
        'currentPage': page,
        'pageSize': 100,
    }
    response = requests.get( 'https://www.vvic.com/apif/samestyle/v3', params=params, headers=headers )
    if response.status_code != 200 :
        return False

    return response.json()['data'][ 'recordList' ]

if __name__ == '__main__':
    conf = getOssPolicy()
    imgLink = uploadImg( conf )
    print( f'图片远程链接：{imgLink}' )

    page = 1
    result = getSearchResult( imgLink, page )
    print( f'第{page}页 搜图商品总数：{len( result ) }' )
    for item in result:
        print( item[ 'item' ] )