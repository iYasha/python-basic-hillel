
# number = input('Enter number: ')

# print(number.isnumeric())
# print(number.isdigit())

# while not (number.isdigit() and int(number) > 4):
#     pass

# A = 2
# B = A
#
# print(hex(id(A)))
# print(hex(id(B)))
#
# A = 2 + 1
#
# print(hex(id(A)))
# print(hex(id(B)))


# list_1 = [2]
# list_2 = list_1
#
# print(hex(id(list_1)))
# print(hex(id(list_2)))
#
# list_1.append(1)
#
# print(hex(id(list_1)))
# print(hex(id(list_2)))

# import sys
#
# A = 'HeLLO world'
# B = 'HeLLO world'
# # C = B
#
# print(hex(id(A)), hex(id(B)))
#
#
# print(sys.getrefcount('HeLLO world'))
#
# del A
#
# print(sys.getrefcount('HeLLO world'))

# import sys
#
# A = []
# B = A
# A.append(B)
#
# print(sys.getrefcount(A))

"""
Найти максимальное число в двумерном списке A
"""

# 1. Работа с двумерным списком

A = [
    [100, 2, 3],
    [4, 120, 6],
    [7, 8, 9]
]

max_number = A[0][0]

# for index in A:
#     for i in index:
#         if i > max_number:
#             max_number = i

# for y, y_value in enumerate(A):
#     for x, x_value in enumerate(y_value):
#         if x_value > max_number:
#             max_number = x_value
#         print(x_value, end=' ')
#     print()
#
# print(max_number)

# 2.

"""
Заполнить двумерный список 3x3 числами от пользователя

[0][0] - 
[0][1] - 
[0][2] - 
[1][0] - 
"""

# X = 3
# Y = 3
# B = []
#
# for j in range(Y):
#     A = []
#     for i in range(X):
#         number = int(input(f'Enter number [{j}][{i}]: '))
#         A.append(number)
#     B.append(A)
#
# print(B)


list_1 = ['Hello', 'world', 'Petya']

# for value in list_1:
#     print(value)
#
# for value in range(len(list_1)):
#     print(list_1[value])

for index, value in enumerate(list_1):
    print(index, value)

