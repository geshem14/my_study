# week 3 task 12
"""
текст задания
Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:
ax + by = e
cx + dy = f
имеет ровно одно решение. Выведите два числа x и y,
являющиеся решением этой системы.
Формат ввода
Вводятся шесть чисел a, b, c, d, e, f
- коэффициенты уравнений системы.
"""
from math import ceil

a1, b1 = float(input()), float(input())
a2, b2 = float(input()), float(input())
c1, c2 = float(input()), float(input())
# вещественные переменные для вводимых чисел

epsilon = 10 ** (-9)  # переменная для заданной точности

determinant_of_equation = a1 * b2 - a2 * b1

if abs(determinant_of_equation) > epsilon:  # если детерминант не равен нулю
    determinant_of_x = c1 * b2 - c2 * b1
    determinant_of_y = a1 * c2 - a2 * c1
    x = determinant_of_x / determinant_of_equation
    y = determinant_of_y / determinant_of_equation
else:
    x = 1
    y = (c1 - a1)/b2
a = x
if abs(ceil(a) - a) < 10 ** -6:
    print(ceil(a), end=" ")
elif abs(ceil(a * 10) - a * 10) < 10 ** -5:
    print('{0:.1f}'.format(a), end=" ")
elif abs(ceil(a * 100) - a * 100) < 10 ** -4:
    print('{0:.2f}'.format(a), end=" ")
elif abs(ceil(a * 1000) - a * 1000) < 10 ** -3:
    print('{0:.3f}'.format(a), end=" ")
elif abs(ceil(a * 10000) - a * 10000) < 10 ** -2:
    print('{0:.4f}'.format(a), end=" ")
elif abs(ceil(a * 100000) - a * 100000) < 10 ** -1:
    print('{0:.5f}'.format(a), end=" ")
else:
    print('{0:.6f}'.format(a), end=" ")

a = y
if abs(ceil(a) - a) < 10 ** -6:
    print(ceil(a))
elif abs(ceil(a * 10) - a * 10) < 10 ** -5:
    print('{0:.1f}'.format(a))
elif abs(ceil(a * 100) - a * 100) < 10 ** -4:
    print('{0:.2f}'.format(a))
elif abs(ceil(a * 1000) - a * 1000) < 10 ** -3:
    print('{0:.3f}'.format(a))
elif abs(ceil(a * 10000) - a * 10000) < 10 ** -2:
    print('{0:.4f}'.format(a))
elif abs(ceil(a * 100000) - a * 100000) < 10 ** -1:
    print('{0:.5f}'.format(a))
else:
    print('{0:.6f}'.format(a))
