#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/10/25 11:53
# @Author : Carey
# @File : 商品详情.py
# @Description

import json
import time
import requests
from urllib.parse import urlparse
import hashlib

t = int( time.time() * 1000 )

headers = {
    'andriodid': '12e7b43fb83ffc1e',
    'os': '2',
    'app-version': '4.91.0',
    'api-sign': '2719a33c9b9924de374b0926d7d69e7d',
    'device-ua': 'Mozilla/5.0 (Linux; Android 9; G576D Build/PQ3A.190605.09291615; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36',
    'user-agent': 'Vvic/5.11.0 (Google+Phone+G576D; Android 9)',
    "userid": '1846988',
    'token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2dmljLmNvbSIsInN1YiI6IntcInVzZXJfaWRcIjpcIjE4NDY5ODhcIixcInRpbWVcIjpcIjIwMjQxMDI1MTQxNTEzNjU2XCJ9In0.qIP5bQT9VCd7ZJyCfVlpG_r9NRnPjR2BKi62nBbc0aPVXx73nAbvTbCF8KwcMzerVsPVf9cBzaCM1z-0_x7stg'
}

url = f'https://app.vvic.com/apif/v1/item?id=49373995&nonce_str=pxyptknwnn&timeStamp={t}'

urlInfo = urlparse( url )

strEnc = f"{urlInfo.path}{urlInfo.query}d1=-d=-aingia=="
sign = hashlib.md5( strEnc.encode(encoding='UTF-8')).hexdigest()

headers[ 'api-sign' ] = sign
response = requests.get( url, headers=headers )

print( response.status_code )
print( response.text )