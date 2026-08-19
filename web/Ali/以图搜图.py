#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/7/8 17:04
# @Author : Carey
# @File : 以图搜图.py
# @Description
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import requests
import time
import execjs
import re
import json
import urllib
import base64

strCookie = 'thw=cn; cna=Uk3xHulLKUUCAT2WC8a/aq/b; mtop_partitioned_detect=1; _m_h5_tk=f9610dcdc6a292aa1a367827f6b72dc8_1746012187485; _m_h5_tk_enc=cf3816a2b95614e373108c3621dc3edd'

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Origin': 'https://s.1688.com',
    'Referer': 'https://www.1688.com',
    'Cookie': strCookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

def upload( imgPath ):

    js_file = "../Tmtb/assets/detail.js"
    with open(js_file, "r", encoding='utf-8') as f:
        js_tamp = f.read()
    jsDrive = execjs.compile(js_tamp)

    with open( imgPath, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())

    strImg = encoded_string.decode('utf-8')

    data = {
        "imageBase64":strImg,
        'appName': 'searchImageUpload',
        'appKey': 'pvvljh1grxcmaay2vgpe9nb68gg9ueg2'
    }

    t = round(time.time() * 1000)
    token = re.findall(r'_m_h5_tk=(.*?)_(?:.*?);', strCookie)
    c = json.dumps(data ).replace(' ', '')
    sign = jsDrive.call('_getSign', token[0], t, c)


    params = {
        'jsv': '2.7.2',
        'appKey': '12574478',
        't': t,
        'sign': sign,
        'api': 'mtop.1688.imageService.putImage',
        'ignoreLogin': True,
        'prefix': 'h5api',
        'v': '1.0',
        'ecode': 0,
        'dataType': 'jsonp',
        'jsonpIncPrefix': 'search1688',
        'timeout': 20000,
        'type': 'originaljson',
    }
    objData = {
        'data': c,
    }

    query = urllib.parse.urlencode( params )
    url = f'https://h5api.m.1688.com/h5/mtop.1688.imageservice.putimage/1.0/?{query}'

    response = requests.post( url=url, headers=headers, data = objData )
    print( response.cookies.get_dict() )
    imgInfo = {
        'id': response.json()[ 'data' ][ 'imageId' ],
        'session': response.json()[ 'data' ][ 'sessionId' ],
    }
    return imgInfo


def getImgSimilar( conf ):

    url = f"https://search.1688.com/service/imageSearchOfferResultViewService?tab=imageSearch&imageAddress=&imageId={conf['id']}&spm=a26352.b28411319.searchbox.input&imageIdList=1080408140072544702&pailitaoCategoryId=10166&beginPage=1&pageSize=40&pageName=image"

    response = requests.get( url, headers=headers )
    print( response.json()['data'][ 'code' ] )
    print( len( response.json()['data']['data'][ 'offerList' ] ) )
    for item in response.json()['data']['data'][ 'offerList' ]:
        info = {
            'id': item[ 'id' ],
            'name': item['information'][ 'subject' ],
            'url': item['information']['detailUrl'],
            'price': item['tradePrice']['offerPrice']['priceInfo']['price'],
            'thumb':  item['image']['imgUrl'],
            'shop_id': item['company']['memberId'],
            'shop_name': item['company']['name'],
            'shop_url': item[ 'company' ][ 'url' ],
            'shop_desrc': f"{item[ 'company' ][ 'bizTypeName' ]} - {item[ 'company' ][ 'province' ]}{item[ 'company' ][ 'city' ]}"
        }
        print( info )

if __name__ == '__main__':
    img = 'abc.jpg'
    imgInfo = upload( img )

    getImgSimilar( imgInfo )