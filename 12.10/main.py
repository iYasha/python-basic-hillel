# import os
# import time

# os.mkdir('/Users/iyasha/Desktop/Test Folder')
# os.rename('test.txt', 'test_2.txt')
# os.remove('test_2.txt')

# print('Hello')
# time.sleep(1)
# print('world')
#
# for i in range(10):
#     print(i)
#     time.sleep(1)
#     os.system('clear')


# file = open('test.txt')

# print(file.read())
# print(file.readlines())
# print(file.readline())
# data = ['Hello world\n', '1\n', '2\n', '3\n']
#
# file = open('test_2.txt', 'wb')

# for i in range(1, 11):
#     for j in range(1, 11):
#         file.write(f'{i} * {j} = {i * j}\n')
# file.write('Hello world\n')
# file.write('123123')
# file.writelines(data)

# print(file.read())
#
# file.close()

import pickle

users = [
    {
        'name': 'Petr',
        'password': 'petr123',
    },
    {
        'name': 'Vasya',
        'password': '@3RS445'
    },
    None,
    True, False
]
#
# f = open('data.pythondata', 'wb')
# pickle.dump(users, f)
# f.write(pickle.dumps(users))
# print(pickle.dumps(users))
# f.close()


# f = open('data', 'rb')

# data = pickle.load(f)
# data = pickle.loads(f.read())
# print(type(data), data)
# f.close()


# with open('data', 'rb') as file_data:
#     print(pickle.load(file_data))
#
#
# print(file_data.read())

import json


# print(type(users), users)
# json_user = json.dumps(users)
# print(type(json_user), json_user)

# with open('data.json', 'w') as f:
#     f.write(json_user)


with open('data.json', 'r') as f:
    json_user = json.loads(f.read())
    print(type(json_user), json_user)

