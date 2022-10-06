import random

# random_numbers = []
#
# for _ in range(10):
#     number = random.randint(1, 100)
#     random_numbers.append(number)
#
# print(random_numbers)
#
# list_comprehension_numbers = [random.randint(1, 100) for _ in range(10) if random.randint(1, 10) % 2 == 0]
#
# print(list_comprehension_numbers)


# numbers = [29, 69, 57, 27, 6, 9, 51, 77, 90, 70]
#
# new_numbers = []
#
# for i in numbers:
#     if i % 3 == 0:
#         new_numbers.append(i)
#
# print(new_numbers)
#
# new_numbers = ''.join([str(i) for i in range(10)])
#
# print(new_numbers)

import sys

# l = [1, 2, 3, 4, 5, 6]
# t = (1, 2, 3, 4, 5, 6) + (7, 8)
#
# t += (8, 9)

# l.append(7)
# t.append(7)

# print(l, type(l), sys.getsizeof(l))
# print(t, type(t), sys.getsizeof(t))
#
# print(t[0])
# print(t.count(3))
# del t[0]


# A = [
#     (1, 2, 3),
#     1, 2
# ]
# print(A)
# B = ('Hello', [1, 2, 3])
# print(B)
# # B[1].append(4)
# B[1] += [4, 5, 6]
# print(B)


# A = {1, 2, 3, 4, 5, 5, 5, 1, 2, 'Hello', 1.5, False, (1, 2, 3)}

# print(hash([1, 2, 3]))
# print(A)

# for item in A:
#     print(item)

# A = {1, 2, 3}
# B = {2, 1, 3, 4, 5, 6}

# print(A.isdisjoint(B))
# print(A == B)
# print(A.issubset(B))
# print(A.issuperset(B))

# A = [1, 2]
# B = A.copy() or [*A] or A[:]
#
# B.append(4)
# print(A, B)

# import copy
#
# A = [
#     [1, 2, 3],
#     [1, 2, 3]
# ]
# # B = A.copy()
# B = copy.deepcopy(A)
#
# # B.append([4,5,6])
# B[0].append(4)
# print(A, B)

# A = {1, 2, 3}
# B = {3, 4, 5}

# C = A.union(B)  # A | B
# print(A, B, C)

# print(A & B, A.intersection(B))

# print(A - B, A.difference(B))
# print(B - A, B.difference(A))

# print(A ^ B, A.symmetric_difference(B))

# A.intersection_update(B)
# A.difference_update(B)
# A.symmetric_difference_update(B)
# print(A)

# A.update(B)


# print(A)
# A.add(123)
# print(A)
# if 1234 in A:
#     A.remove(1234)
# A.discard(1234)
# print(A.pop())
# A.pop()
# print(A)

# print(A)
#
# iter_obj = iter(A)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# numbers = [123, 2, 3, 4, 1]
# # numbers = []
#
# if len(numbers) > 0:
#     print(numbers[0])
#
# first_obj = next(iter(numbers), None)
# print(first_obj)


# A = frozenset({1, 2, 3})
# print(A)


# A = {'Petr'}
A = {
    'name': 'Petr',
    'mark': {
        '19.09': {
            'value': 80,
            'description': '...'
        },
        '29.09': 100,
        '05.10': 99
    },
    'email': 'petr@gmail.com',
    'visits': [True, False, True, True],
    (1, 2, 3): 'Hello',
}

# print(A['name'])
# print(A['mark']['29.09'])
# print(A['email'])
# print(A['visits'])
# A['visits'].append(False)
# print(A['visits'][0])
# print(A['visits'])
# print(A[(1, 2, 3)])
# print(A)

# for i in A:
#     print(i)
#
# for key, value in A.items():
#     print(key, value)

# print(A['discount'])
# print(A.get('discount', True))

# contacts = []
# template = {
#     'name': ...,
#     'phone': ...,
#     'additional_contacts': [...],
# }
# contacts.append(template)

# students = [
#     {
#         'name': 'Petr',
#         'mark': {
#             '19.09': {
#                 'value': 80,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'petr@gmail.com',
#         'visits': [True, False, True, True],
#     },
#     {
#         'name': 'Vasya',
#         'mark': {
#             '19.09': {
#                 'value': 100,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'vasya@gmail.com',
#         'visits': [True, True, True, True],
#     },
# ]

# for contact in students:
#     print(contact['name'])

contact = {
    'name': 'Petr',
    'email': 'petr@gmail.com',
    'additional_contacts': ['88823443'],
}
# contact_2 = contact
#
# contact['name'] = 'Vasya'
#
# print(contact, contact_2)
# contact['email'] = 'petr123@example.com'

# contact.update({
#     'email': 'petr123@example.com',
#     'additional_contacts': [],
#     'age': 30,
# })
# contact['age'] = 32
# print(contact)
# print(contact.fromkeys(['key_1', 'key_2', 'key_3'], None))
# del contact['age']
# print(contact.pop('age1', None))
# print(contact.popitem())
# print(contact.setdefault('age', 30))
# print(contact.values())
# print(contact)


