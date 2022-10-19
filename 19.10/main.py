

# with open('big_data.txt', 'w') as f:
#     for i in range(1000000):
#         f.write(f'Data #{i}\n')

# ID,Name,Email
# 1,Petr,petr@gmail.com
# 2,Vasya,vasya@gmail.com

# with open('big_data.txt', 'r') as f:
#     big_data = f.readline()
#     print(big_data)
#     exit()
#
# print(len(big_data))


# def number_generator(n=10):
#     numbers_sum = 0
#     for i in range(n):
#         numbers_sum += i
#         yield numbers_sum
#     print('Stop iteration')
#
# generator = number_generator(1000000)
#
# while generator:
#     try:
#         print(next(generator))
#     except StopIteration:
#         print('End')
#         break

# from random import *
# from core.utils import *
# from core import utils

# utils.greetings('Petr')
# print(randint(1, 5))


class Person:
    lists = []
    instance_count = 0

    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies.split(', ')
        self.file = open(f'data_{self.name.lower()}.json', 'w')
        Person.lists.append(self.name)
        Person.instance_count += 1

    def __del__(self):
        print(f'Delete {self.name}')
        self.file.close()

    def get_name(self):
        return self.name

    def print_id(self):
        self.file.write(f'{self.name} - {hex(id(self))}')
        print(f'{self.name} - {hex(id(self))}')

    def print_hobbies(self):
        self.print_id()
        print(f'{self.name} likes ')
        print('\n'.join(self.hobbies))

print(f'Lists: {Person.instance_count}')
tom = Person('Tom', 25, 'Tennis, football, TV')
bob = Person('Bob', 30, 'YouTube, Music')

print(f'Lists: {Person.instance_count}')
# tom.print_hobbies()
# print(hex(id(tom)))
tom.print_id()

del tom

bob.print_id()

# for i in range(1000):
#     print(i)

# tom.print_hobbies()
# print('----------')
# bob.print_hobbies()


"""
 0 | X | X | 
"""

