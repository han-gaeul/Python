import json
from pprint import pprint

# 파일을 열고

f = open('stocks.jons', 'r', encoding = 'urf-8')
# json을 파이썬 객체 형식으로 한다
kospi = json.load(f)
print(kospi['stocks'][0])
samsung = kospi['srocks'][0]
print(samsung, type(samsung))