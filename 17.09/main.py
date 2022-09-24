# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# is_even = 'Even' if number % 2 == 0 else 'Odd'

# print('Even' if number % 2 == 0 else 'Odd')

# number = 3
# condition = False
#
# if number % 2 == 0:
#     print(10)
# else:
#     if condition:
#         print(20)
#     else:
#         print(30)
#
# print(10) if number % 2 == 0 else print(20) if condition else print(30)

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# number = int(input('Enter number: '))
#
# while not 0 <= number <= 10:
#     print('Ошибка!')
#     number = int(input('Enter number: '))
#
# print('Получили правильное число!')


# while True:
#     number = int(input('Enter number: '))
#
#     if 0 <= number <= 10:
#         break
#
#     print('Ошибка')
#
# print('Получили правильное число!')

# number = 0
#
# while number != 100:
#     number += 1
#
#     if number % 2 != 0:
#         continue
#
#     print(number)
#
#
# print('Конец цикла!')


# number = 0
#
# while number < 49:
#     number += 3
#
#     if number == 50:
#         break
#
#     print(number)
#
# else:
#     print('Цикл завершился успешно!')
#
#
# print('Конец цикла!')


"""
1) Пользователя вводит два числа A и B, нужно вывести сумму чисел в диапазоне от A до B.
"""

# A = int(input('Enter number #1: '))
# B = int(input('Enter number #2: '))
# summ = 0
#
# # A = 10
# # B = 4
# if A > B:
#     print('error!')
#     exit(4)
# if A > B:
#     A, B = B, A
#
#
# while A < B:
#     summ += A
#     A += 1




"""
2) Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
"""

# A = int(input('Enter number #1: '))
# B = int(input('Enter number #2: '))
# summ = 0
#
# while A < B:
#     if A % 2 == 0:
#         summ += A
#         print(A)
#     A += 1
#
# print(summ)

"""
3) Пользователь вводит два числа A и B, нужно вывести прямоугольник со сторонами A и B с помощью символа '*' используя цикл.
В коде можно использовать символ '*' только один раз.
"""

# A = int(input('Enter number #1: '))
# B = int(input('Enter number #2: '))
# main_symbol = '*'
# temp = 0

"""
A = 4
B = 5

****
****
****
****
****

main_symbol * A
"""

# print((('*' * A) + '\n') * B)

# while temp < B:
#     i = 0
#     while i < A:
#         print(main_symbol, end='')
#         i += 1
#     print()
#     temp += 1
#
#
# while temp < B:
#     print(main_symbol * A)
#     temp += 1



"""
4) Запросить у пользователя число N, вывести треугольник шириной N используя символ '*'.
Input:
N = 6
Output:
6 ******
5 *****
4 ****
3 ***
2 **
1 *
"""

N = int(input('Enter number: '))
main_symbol = '*'

while N > 0:
    print(main_symbol * N)
    N -= 1
















"""
1) Запросить у пользователя число N, вывести все числа от 0 до N которые делятся на 3.
"""


# N = int(input('Enter number: '))
# number = 0

# while number < N:
#
#     if number % 3 == 0:
#         print(number)
#
#     number += 1


# while number < N:
#     print(number)
#     number += 3



















