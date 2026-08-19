#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/10/24 9:51
# @Author : Carey
# @File : 商品详情.py
# @Description
import time
import requests
import hashlib
import random
import string

def get_uidid( length ):
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string.lower()


def getTimeCode( param ):
    if not param or len( param ) <= 0:
        return None

    sc = 'MC0CAQACBQC5FhxRAgMBAAECBF94RXkCAwDlNwIDAM63AgMAp7kCAwC9hwICR5c='
    str = f"{param[ 'action' ]},{param['timestamp']},{sc},{param['udid']}"

    sign = hashlib.md5( str.encode(encoding='UTF-8') ).hexdigest()
    return sign


pid = 1555896865
iTime = int( time.time() * 1000 )

params = {
    'pid': pid,
    'access-token': None,
    'union_id': '537-27',
    'img_size': 'h',
    'user_client': 'android',
    'action': 'get_product',   # get_product -商品主体，get_product_html -商品详情
    'client_version': '8.2.1',
    'udid': get_uidid( 32 ),
    'timestamp':iTime,
}
params[ 'time_code' ] = getTimeCode( params )

url = 'http://product.mapi.dangdang.com/index.php'
request = requests.get( url, params=params )
print( request.status_code )
print( request.text )


