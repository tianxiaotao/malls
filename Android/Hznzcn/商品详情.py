#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description
from Crypto.Cipher import DES
import base64
import requests

class DESUtil():
    def __init__(self, key, mod ):
        self.key = key
        self.mode = mod

    def unpadding(self,data_e):  # 参数data_e是byte形式的、已经填充的data
        data_e = data_e[:-data_e[-1]]  # 去掉填充，这里直接去掉data_e的最后一位的值对应的长度，因为之前填充的填充位就是填充长度的数字（读起来太绕的话建议直接执行一下试试看效果，但要注意这里是【byte类型】才可以实现这种操作！）
        return data_e.decode()  # byte转str

    def decrypt(self, data):
        key = self.key.encode()
        data = base64.b64decode( data )  # b64decode传入参数可以是str，返回的是byte，所以这里执行后，data也是byte了
        des = DES.new(key, self.mode )
        data = des.decrypt(data)  # 解密得到的是明文经填充了的结果，byte类型
        result = self.unpadding( data )  # 去掉填充，str类型
        return result


headers = {
    'Accept':'application/json',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'hbt-android',
}

pid = 24354412

params = {
    'ProId': pid,
    'IsWantSpec': 1,
    'IsWantAlbum': 1,
    'IsWantSpecImg': 1,
    'IsWantVideo': 1,
    'IsWantContent': 1,
    'IsWantProps': 1,
    'IsWantMarketingProduct': 1,
    'IsWantDTC': 1,
    'api_versions': 53,
    'request_device_type': 2,
    'ProFromId': None,
    'APCType': 3,
}
url = f'https://app-h5.hznzcn.com/server/Search/ProductDetail'

requests = requests.post( url, data= params, headers=headers )
encData = requests.json()['EncryptInfo'].strip()

des = DESUtil( '20200812', DES.MODE_ECB )
desDatas = des.decrypt( encData )
print( desDatas )

