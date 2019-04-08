#-*- coding: utf-8 -*-

from urllib.request import urlopen

import bs4, json
from plugins import key_config

currency_code = {
    '중국': 'CNY',
    '한국': 'KRW',
    '일본': 'JPY',
    '홍콩': 'HKD',
    '미국': 'USD',
    '베트남': 'VND',
    '대만': 'TWD'
}

def run(currency):
    key = "%s_KRW" % (currency_code[currency])
    url = "https://free.currencyconverterapi.com/api/v6/convert?q=%s&compact=ultra&apiKey=%s" % \
          (key, key_config.CURRENCYCONVERTERAPI)

    with urlopen(url) as response:
        try:
            res = response.read()
            r = json.loads(res)
            body_res = "[환율] **%s** => 한국: **%s** KRW" % (currency, r[key])
        except Exception as e:
            print(e)

    r = {"body":body_res}
    return r