#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/4/3 17:22
# @Author : Carey
# @File : __init__.py.py
# @Description
import random

from config import account


def getAccInfo():
    index = random.randint( 0, len( account ) -1 )

    return account[index]