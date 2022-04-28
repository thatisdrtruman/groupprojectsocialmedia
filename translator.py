# /usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
import random
import requests


def getTransText(in_text):
    q = in_text
    fromLang = 'auto'  # origin language = auto detect
    toLang1 = 'en'  # translated language = English

    appid = '20210305000716079'  # APP ID
    appkey = 'EdH0X4XEIi8LjEsKiyTb'  # Key
    salt = random.randint(32768, 65536)  # generate salt

    # generate sign
    sign = appid + q + str(salt) + appkey
    # calculate sign(md5 encryption, note before encryption, m1 must be UTF-8 coding)
    m1 = hashlib.md5(sign.encode('utf-8'))
    sign = m1.hexdigest()

    # generate full request
    myurl = '/api/trans/vip/translate'
    myurl = (myurl + '?appid=' + appid + '&q=' + q +
             '&from=' + fromLang + '&to=' + toLang1 + '&salt=' +
             str(salt) + '&sign=' + sign)
    url = "http://api.fanyi.baidu.com" + myurl

    # send request
    url = url.encode('utf-8')
    res = requests.get(url)

    # transform to dic
    res = eval(res.text)
    return res['trans_result'][0]['dst']
