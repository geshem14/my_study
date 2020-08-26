# week 4 task 6
"""
текст задания                                                 тут 79 символ=>!
Даны пять действительных чисел: x, y, xc, yc, r.
Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
возвращающую True, если точка принадлежит кругу и False, если не принадлежит.
Основная программа должна считать координаты точки,
вызвать функцию IsPointInCircle и в зависимости от возвращенного значения
вывести на экран необходимое сообщение. Функция IsPointInCircle
не должна содержать инструкцию if.
Формат ввода - Вводится пять действительных чисел.
"""
from math import sqrt

x, y, cx, cy, r = float(input()), float(input()), \
                  float(input()), float(input()), float(input())


def a_Les_Or_Equal_b(a, b):
    """
    функция сравнивает два вещественных числа и возвращает ИСТИНА
    если а меньше либо равно в
    """
    epsilon = 10 ** (-9)
    return a + epsilon <= b or abs(a - b) < epsilon


def IsPointInCircle(d_x, d_y, d_cx, d_cy, d_r):
    """
    функция использует функцию сравнения дествительных чисел и возвращающее
    логический результат
    """
    distans_from_point_to_center = sqrt((d_x - d_cx) ** 2 + (d_y - d_cy) ** 2)
    temp_boolean_1 = a_Les_Or_Equal_b(distans_from_point_to_center, d_r)

    return temp_boolean_1


if IsPointInCircle(x, y, cx, cy, r):
    print("YES")
else:
    print("NO")
