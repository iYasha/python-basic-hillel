
# class Foo:
#
#     def __init__(self, name):
#         self._bar = name
#
#     def __del__(self):
#         print(f'del {self._bar}')
#
#
# f1 = Foo('f1')
# f2 = Foo('f2')
#
#
# del f2
#
# input()


# from pprint import pprint
#
#
# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'name': 'Ivan',
# }
#
# pprint(d)

import json
import requests
import time
import os

# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#
#
# while True:
#     start = time.time()
#     response = requests.get(url)
#     print(f'{response} - took {time.time() - start}s')
#     # print(response)
#
#     data = response.json()
#
#     # for item in data:
#     #     print(f'CCY - {item["ccy"]}')
#     #     print(f'BUY - {item["buy"]}')
#     #     print(f'SALE - {item["sale"]}')
#     #     print('==========================')
#     time.sleep(3)


# url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

# while True:
#
#     resp = requests.get(url)
#
#     if not 200 <= resp.status_code <= 299:
#         print(resp.content)
#         break
#
#     data = resp.json()
#     os.system('clear')  # cls
#     print(f'{data["symbol"]} = {data["price"]}')
#     time.sleep(1)


from typing import Union
import enum


class BinanceRequestError(ValueError):
    pass


class SymbolPrice:

    def __init__(self, symbol: str, price: Union[int, float, str]):
        self.symbol = symbol

        self.price = price
        if isinstance(price, (int, str)):
            self.price = float(price)

    def __str__(self):
        return f'Symbol = {self.symbol} | Price = {self.price}'


class SymbolEnum(enum.Enum):
    BITCOIN = 'btcusdt'
    ETH = 'ethbtc'


class Binance:

    def __init__(self, symbol: Union[str, SymbolEnum]):
        self.symbol = str(symbol)

    def is_success(self, status_code: int) -> bool:
        return 200 <= status_code <= 299

    def get_price(self) -> SymbolPrice:
        resp = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}')
        if not self.is_success(resp.status_code):
            raise BinanceRequestError(resp.content.decode())
        return SymbolPrice(**resp.json())


bitcoin = Binance(SymbolEnum.BITCOIN)
print(bitcoin.get_price())
