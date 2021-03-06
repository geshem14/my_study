# week 4 task 9
"""
текст задания                                                 тут 79 символ=>!
Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
Решение оформите в виде функции MinDivisor(n).
Алгоритм должен иметь сложность порядка корня квадратного из n.

Указание. Если у числа n нет делителя не превосходящего корня из n,
то число n — простое и ответом будет само число n. А у всех составных
чисел обязательно есть делители,
отличные от единицы и не превосходящие корня из n.
"""
from math import sqrt
n = int(input())  # целочисленная переменная  для ввода


def MinDivisor(d_n):
    """
    функция возвращает наименьший делитель числа
    """
    i = 2  # индекс для оператора while
    while i <= d_n:
        if d_n % i == 0:
            return i
        elif i >= sqrt(d_n):
            return d_n
        else:
            i = i + 1


print(MinDivisor(n))
