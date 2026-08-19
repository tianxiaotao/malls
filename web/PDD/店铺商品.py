#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/5/15 17:33
# @Author : Carey
# @File : shopProductsOld.py
# @Description
import requests
import execjs
from reverse.Mall.PDD import getAccInfo

uinfo = getAccInfo()
print( uinfo )

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://mobile.yangkeduo.com/mall_page.html?mall_id=773565015',
    'Cookie': f"webp=1; PDDAccessToken={uinfo['token']}; pdd_user_id={uinfo['uid']}; pdd_vds=gaLLNOQGEynQyNmOaoQPEimQLbnoyEbOaaPEiLiPbtOOELQPGNPaanbLOQOi",
    'rfp': 'NkmtzR3ScAijfoJAwNTBNdR4PBWtHFS2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
    'xweb_xhr': '1',
}

with open("pdd_ant.js", "r") as f:
    ant = f.read()
antDrive = execjs.compile( ant )
objResult = antDrive.call( 'getPddAntContent' )

params = {
    'pdduid': '6789722353',
    'anticontent': objResult[ 'ant' ],
    'category_id': 0,
    'type': 0,
    'mall_id': 773565015,
    'page_size': 20,
    'sort_type': 'default',
    'refer_page_param': 'undefined',
    'msn': 'frdwu7rkr6ljczj67yzplve7se_axbuy',
    'flip': '',
    'list_id': 'tcqwe0xgleprxpuq',
    'page_from': 39,
    'query': '',
    'new_store_goods': '',
    'show_priority_type': 1,
    'show_condition': 'null',
    'data_type_list': 1,
    'pair_goods_id_list': '',
    'filter_condition': '',
    'query_shipping_option': 1,
    'card_num_after_last_card': [],
    'card_num_total': None,
    'page_no': 2,
}

response = requests.get( 'https://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods', params=params, headers=headers, )
print( response )
print( response.text )
