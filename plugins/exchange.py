#-*- coding: utf-8 -*-

from urllib.request import urlopen

import bs4, json
from plugins import key_config

currency_code = {
    '중국': 'CNH',
    '일본': 'JPY(100)',
    '홍콩': 'HKD',
    '미국': 'USD',
    '싱가포르': 'SGD',
    '싱가폴': 'SGD'
}

def run(currency):
    key = currency_code[currency]
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=%s&searchdate=&data=AP01" % \
          (key_config.CURRENCY_EXCHANGE_API_KEY)
    print(url)
    try:
        with urlopen(url) as response:
            res = response.read()
            r = json.loads(res)
            for result in r:
                if result['cur_unit'] == key:
                    break
            body_res = "**%s %s**\n팔때: %s KRW\n살때: %s KRW\n매매 기준: %s KRW" % \
                       (currency, key, result['ttb'], result['tts'], result['deal_bas_r'])
    except Exception as e:
        body_res = "서버 오류로 응답할 수 없습니다."
        print(e)

    r = {"body":body_res}
    return r