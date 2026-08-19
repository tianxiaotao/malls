#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description

import requests


headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Referer':'https://www.vvic.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Cookie': 'source=m;userLoginAuto=1;vvic_token=xxxxxxxx-1d9b-4815-8c34-xxxxxxx;uid=00000;userName=vvic915300000;umc=1;pn=0'
}


def getItemByPC( slug ):
    url = f'https://www.vvic.com/apif/item/{slug}/detail'
    response = requests.get( url, headers=headers )
    print( response )
    #print( response.text )
    data =  response.json()[ 'data' ]

    print( f"{data['id']} --- {data['title']} --- {data['price']}" )


def getItemByM( slug ):
    headers[ 'Host' ] = 'app.Vvic.com'
    headers[ 'Referer' ] = 'https://app-h5.vvic.com/'
    headers[ 'platform' ] = 'm'
    headers[ 'app-version' ] = 'mobile'
    headers['platform'] = 'm'
    headers[ 'User-Agent' ] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'

    url = f'https://app.vvic.com/apif/v1/item?id={slug}'
    response = requests.get( url,  headers=headers)

    print(response)
    #print(response.text)

    data = response.json()['data'][ 'item' ]

    print(f"{data['id']} --- {data['title']} --- {data['price']}")


if __name__ == '__main__':
    slug = '65e59166ed83e3000852e20b'

    getItemByPC( slug )
    getItemByM( slug )
