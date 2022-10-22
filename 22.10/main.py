

class Item:

    def __init__(self, name: str, position: int):
        self.name = name
        self.position = position


class ItemController:

    def __init__(self):
        self.items = []

    def add_item(self, obj: list, name: str, position: int) -> list:
        pass

    def delete_item(self, obj: list, position: int) -> list:
        pass


"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, 
что задано положительное целое число).
"""
# cp1256
# utf-8


def read_last(line_count: int, file: str):
    if line_count <= 0:
        return

    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        from_slice = len(lines) - line_count
        output = ''.join(lines[from_slice:])
        print(output)


# tmp = 'Привет'
#
# bytes_str = tmp.encode('utf-8')
# print(bytes_str.decode('cp1256'))

# from dateutil import parser
#
# print('Hello')
# now_date = datetime.now()
# print(now_date.strftime('Year - %Y | Month = %m | Hours = %H'))
# print(now_date.strftime('%Y-%m-%d %H:%M:%S'))
# user_date = datetime.strptime('2021-01-0112:00:00', '%Y-%m-%d %H:%M:%S')

# print(parser.parse('2021-01-01 12:00:00'))
# print(type(user_date), user_date)


from datetime import datetime


# class Animal:
#     __available_animals = ('dog', 'cat', 'bird')
#
#     def __init__(self, name: str, age: int, animal_type: str):
#         if animal_type not in self.__available_animals:
#             raise ValueError('Animal type is not available')
#         self.name = name
#         self.age = age
#         self.__animal_type = animal_type
#
#     def get_birthday_year(self) -> int:
#         return datetime.now().year - self.age
#
#     def make_sound(self):
#         if self.__animal_type == 'dog':
#             print('Woof!')
#         elif self.__animal_type == 'cat':
#             print('Meow!')
#         elif self.__animal_type == 'bird':
#             print('Chirp!')

import abc


class Animal(abc.ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_birthday_year(self) -> int:
        return datetime.now().year - self.age

    @abc.abstractmethod
    def make_sound(self):
        pass


class AnimalInterface(abc.ABC):

    @abc.abstractmethod
    def make_sound(self):
        pass

    @abc.abstractmethod
    def get_birthday_year(self) -> int:
        pass


class Dog(Animal):

    def make_sound(self):
        print('Woof!')

    def play(self):
        print('Playing with a ball')


class Cat(Animal):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print('Meow!')


class Bird(Animal):

    def make_sound(self):
        print('Chirp!')


class Fish(Animal):

    def make_sound(self):
        print('Blub!')


class Car:

    def __init__(self, name: str, model: str, year: int):
        self.name = name
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.name} {self.model} {self.year}'

    def __int__(self):
        return self.year

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.year > other.year
        elif isinstance(other, int):
            return self.year > other

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.year < other.year
        elif isinstance(other, int):
            return self.year < other

    def __len__(self):
        return len(self.name)


# class A(object):
#
#     def foo(self):
#         print('A.foo')
#
#
# class B(A):
#     b = 1
#
#     def foo(self):
#         print('B.foo')
#
#
# class C(A):
#     c = 2
#
#     def foo(self):
#         print('C.foo')
#
#
# class D(B, C):
#
#     def foo(self):
#         super().foo()
#         print('D.foo')
#
#
# d = D()
# d.foo()
# print(d.b, d.c)


# dog = Dog('Rex', 5)
# cat = Cat('Tom', 3, 'Blue')
# bird = Bird('Tweety', 1)
# fish = Fish('Nemo', 2)
#
# dog.play()
# fish.make_sound()
# print(cat.color)


# def print_animals_sound(animals: list):
#     for animal in animals:
#         if isinstance(animal, Animal):
#             animal.make_sound()
#         else:
#             print(f'{animal} is not an animal')
#
#
# animals = [Dog('Rex', 5), Cat('Tom', 3, 'Blue'), Car('Tesla', 'Model Y', 2017), Bird('Tweety', 1), Fish('Nemo', 2)]
# print_animals_sound(animals)


list_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

list_2 = [
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 1]
]

list_3 = list_1 + list_2

list_3 = [
    [2, 3, 4],
    [5, 7, 7],
    [8, 9, 10]
]


car = Car('Tesla', 'Model Y', 2017)
car_2 = Car('BMW', 'X5', 2019)

print(car < 2020)
print(len(car_2))


