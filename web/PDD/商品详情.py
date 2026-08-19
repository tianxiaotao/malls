#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/14 9:54
# @Author : Carey
# @File : PyCharm 音频下载.py
# @Description
import requests
import execjs
from reverse.Mall.PDD import getAccInfo

uinfo = getAccInfo()
print( uinfo )

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://mobile.yangkeduo.com/index.html',
    'Cookie': f"webp=1; PDDAccessToken={uinfo['token']}; pdd_user_id={uinfo['uid']}",
    'rfp': 'NkmtzR3ScAijfoJAwNTBNdR4PBWtHFS2',
    'User-Agent': 'android Mozilla/5.0 (Linux; Android 9; 23116PN5BC Build/PQ3A.190605.09291615; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36  phh_android_version/7.29.0 phh_android_build/36ae8271156ef33d708399a27900669b93dae6de phh_android_channel/main_doudi pversion/0',
    'xweb_xhr': '1',
}

params = {
    'pdduid': {uinfo['uid']},
    'xcx': '20161201',
    'xcx_version': 'v8.3.40',
    'xcx_hash': '1708567390705kKYXCYjA8i9lHqF2',
}

with open("pdd_ant.js", "r") as f:
    ant = f.read()
antDrive = execjs.compile( ant )
objResult = antDrive.call( 'getPddAntContent' )

json_data = {
    'goods_id': '526748291294',
    'page_version': 7,
    'client_time': objResult['time'],
    'anti_content': objResult['ant'],
    'xcx_version': 'v8.3.40',
}
response = requests.post('https://api.pinduoduo.com/api/oak/integration/render', params=params, headers=headers, json=json_data)
print( response.text )
