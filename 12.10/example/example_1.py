
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution 1 - O(1)
last_item = data[-1]

# Solution 2 - O(n)
summ = 0
for item in data:
    summ += item

# Solution 3 - O(n^2)
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')

# Solution 4 - O(n)
min_number = data[0]
for item in data:
    if item < min_number:
        min_number = item

max_number = data[0]
for item in data:
    if item > max_number:
        max_number = item

# Solution 5 - O(n^2)
N = 50
for i in range(N):
    for j in range(N):
        for k in range(1000):
            print(i + j + k)

# Solution 6 - O(n^2)
items = [10, -1, 2, 3, 6, 2, 7, 8, -20]

for i in items:
    print(f'value = {i} | count = {items.count(i)}')




