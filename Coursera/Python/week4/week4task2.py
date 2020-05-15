# week 4 task 2
"""
текст задания                                                 тут 79 символ=>!
Даны четыре действительных числа: x₁, y₁, x₂, y₂.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""
from math import ceil

x1, y1, x2, y2 = float(input()), float(input()), \
                 float(input()), float(input())


def distance(d_x1, d_y1, d_x2, d_y2):
    """
    функция возвращает расстояние между двумя точками заданными координатами
    """
    distance_between_of_points = ((d_x2 - d_x1) ** 2 +
                                  (d_y2 - d_y1) ** 2) ** (1 / 2)
    return distance_between_of_points


def print_float(a):
    """
    функция печатает вещественные числа со значимой размерностью
    то есть число 1.0 напечатается как 1
    число 1.25 так и напечатается
    максимальная размерность печати 10 ** 5
    """
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
    else:
        print('{0:.5f}'.format(a), end=" ")


print_float(distance(x1, y1, x2, y2))
