#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/12/31 16:44
# @Author : Carey
# @File : x.py
# @Description
import json

import requests
import time


iTime = round( time.time() * 1000 )

headers = {
    'timestamp': str( iTime ),
    'fingerprint': 'c641b04643f6d2a2',
    'content-type': 'application/json; charset=utf-8',
    'user-agent': 'okhttp/4.12.0',
}

json_data = {
    'version': {
        'appType': 'android',
        'appVersion': '4.127.1',
        'osType': 'android',
        'osVersion': '9',
        'osLevel': '28',
        'hardwareType': 'phone',
        'hardwareModel': 'Google Phone G576D',
        'hardwareYearClass': '2016',
        'androidInfo': {
            'screen': {
                'widthPixels': 720,
                'heightPixels': 1280,
                'densityDpi': 320,
                'scaledDensity': 2.0,
            },
            'hardware': {
                'brand': 'Google Phone',
            },
        },
        'legalEntity': 'jmt',
    },
}
response = requests.post('https://api.joom.com/1.1/device/create', headers=headers, json=json_data)

print( response )
print( response.text )

accToken = response.json()[ 'payload' ][ 'accessToken' ]
refToken = response.json()[ 'payload' ][ 'refreshToken' ]

# accToken = 'SEV0001AHf82pbsJxjj6f803uRxytXlBcQugEweXyOWr2cGqCAEA_k3uFzhidO5gSxg7jEj38ULVubTKzMuOBXElkYSdPvJ5HsVh13CisLEgBQlD7X_fZDW4Qq8nzEl-rtTZC7aAyuq2HCCersJSBYCUZQEhVijnPwrvFE1GRnrYF2E1nO0PgTGPEgvD8YRZrMLLgVJZi59giobg63Cr3HNgtGHiuA9VSIoxAne1-bjw6VVsfd24tg'
# refToken = 'SEV0001AHf82pbsJxjVx-P_OZNPKsZMBvctLpNMHbQ-0fdk-xC-znNX3WjhPA0uvCxseYuv9Cm6k7ElumFMtT4u1FT_cZmd2hmIPJrcq2El8PmZnFJqvc6cwQiLSPWFR1Wps7egQJ8enPqM2PMz9FRVoJNL2ejuBATvjUAbTrFYo8nuHl_PMdoJyDv_A5HtkZC2gtp3v0l5it627L4W'

headers = {
    'authorization': f'Bearer {accToken}',
    'content-type': 'application/json; charset=UTF-8',
    'app-config-id': '8be2b1bfea756e37694175c3f48f145d',
    'fingerprint': 'c641b04643f6d2a1',
    'user-agent': 'okhttp/4.12.0',
}
data = {
    'refreshToken': refToken,
}
response = requests.post('https://api.joom.com/1.1/device/token/refresh',  headers=headers, data=json.dumps( data ) )

print( response )
print( response.text )
print( response.headers )


joomAccToken = response.headers.get( 'joom-set-access-token' )
joomRefreshToken = response.headers.get( 'joom-set-access-token' )

headers[ 'authorization' ] = f'Bearer {joomAccToken}'

params = {
    'sDV': 'newArrivalsProductsConfig',
}

repData = {
    'appearance': {
        'productColumns': 2,
        'featuredBrandColumns': 3,
        'featuredCategoryColumns': 3,
        'bannersColumns': {
            'smallImage': 3,
            'largeImage': 2,
        },
        'productCardColumns': {
            'smallCard': 3,
            'largeCard': 2,
        },
        'productCollectionColumns': 2,
        'selectableProductCollectionColumns': 3,
    },
}

response = requests.post( 'https://api.joom.com/1.1/contentList/promotedProducts/get', params=params, headers=headers, data=json.dumps( repData ) )
#
print( response )
print( response.text )




json_data = {
    'openPayload': {
        'isVerticalScroller': True,
        'place': 'search',
    },
    'skipPaging': True,
    'skipItems': False,
    'options': {
        'supportAsyncVariants': False,
    },
}

detail = requests.post( 'https://api.joom.com/1.1/products/601a3de2fbf56701063807b0/contentList/get', headers=headers, json=json_data )

print( detail )
print( detail.text )
