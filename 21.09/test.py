"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'

1. isspace
2. islower
3. isupper
4. isdigit
"""

test_string = 'Hello world123'

for symbol in test_string:
    print(symbol)
    print(symbol.isspace())
    print(symbol.islower())
    print(symbol.isupper())
    print(symbol.isdigit())
    print('======================')