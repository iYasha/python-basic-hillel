"""
Строки
"""

# name = 'Petr !1234'
# print('Hello' + ' world')
# print('Hello' * 3)
# print(len(name))


string = 'Hello world'
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])
# print(string[6])
# print(string[1:4])
# string[от:до:шаг]
# print(string[5::2])
# print(string[::-2])
# print(string[-3:-1])
# print(string[-1])
# print(string[-3])
# print(string[len(string) // 2])

# f'F-string'
# b'Bytes-string'
# r'Regexp-string'

# symbol_index = 'Hello world'.find('o')
# next_symbol_index = 'Hello world'.find('o', symbol_index + 1)
# rfind_symbol_index = 'Hello world'.rfind('123')
# print(symbol_index)
# print(next_symbol_index)
# print(rfind_symbol_index)
#
# user_string = input('Enter your string: ')
# user_substring = input('Enter your substring: ')
#
# symbol_index = user_string.index(user_substring)
#
# if symbol_index != -1:
#     print('Yes')
# else:
#     print('No')


url = input('Enter URL: ')

if url.startswith('https://') and url.endswith('.com'):
    print('Correct!')
else:
    print('Error')


