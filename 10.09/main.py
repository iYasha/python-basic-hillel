
# a = 5
# b = a
#
# print(hex(id(a)))
# print(hex(id(b)))
#
# a = 6
# print(a, b)
#
# print(hex(id(a)))
# print(hex(id(b)))


data = '2515'

print(data.isnumeric())  # Возвращает True если в строке все символы - числа, иначе False

# print(type(10))
# print(type(data))
data = int(data)
print(type(data))

"""
Преобразование типов данных:
 - int
 - float
 - bool
 - str
"""

# number = int(input('Number 1:'))
# number2 = int(input('Number 2:'))
#
# print(type(number), type(number2))
#
# print(f'Result: {number + number2}')

# print(True + True + True + False)
# print(bool(0))


a = 10 / 2

print(a, type(a))
print(2.0 + 3)
print(int(2.5))
print(round(2.6))
