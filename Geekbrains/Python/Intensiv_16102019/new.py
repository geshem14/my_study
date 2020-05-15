# https://geekbrains.ru/lessons/51092

import sys
import copy

a = [15, 574.2, 'hello', True, "world"]
print(type(a))  # type

# getter
# setter?
a[0] = 13
print(a)
# mutable
# immutable

print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))

print(dir(a))
a.append('cool')
print(a)

a.remove('cool')
print(a)

b = (13, 574.2, 'hello', True, "world")
print(b)
c = copy.deepcopy(a)
print(c)
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

print(dir(b))
print()

print("_________________ Пример с матрицей_____________________")
matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

matrix_t = list(zip(*matrix))
# matrix_t = list(zip(
#     matrix[0],
#     matrix[1],
#     matrix[2],
#     matrix[3],
#     matrix[4],
# ))

# print(matrix)

for row in matrix:
    print(row)

print('*' * 17)
for item in matrix_t:
    print(list(item))
print()

print("________________Пример с zip _________________")
# zip map filter
days = ('пн', 'вт', 'ср', 'чт')
energy_1 = (1584.5, 596.5, 2417.6, 3695.5)
energy_2 = (6587.2, 148.3, 6547.2, 2473.2)

# ('пн', 1584.5, 6587.2), ...
# result = list(zip(days, energy_1, energy_2))
# print(result)

args = (days, energy_1, energy_2)
result = list(zip(*args))
print(result)
