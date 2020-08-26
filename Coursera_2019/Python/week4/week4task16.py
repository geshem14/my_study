# week 4 task 16
"""
текст задания                                                 тут 79 символ=>!
Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть выведите два других числа p и q таких,
что (n / m) = (p / q) и дробь (p / q) — несократимая.
Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
Формат ввода
Вводятся два натуральных числа.
"""

n, m = int(input()), int(input())  # переменные  для ввода


def LeastCommMultip(d_a, d_b):
    """
    функция возвращает наименшее общее кратное двух натуральных цисел
    """
    if d_b == 0:
        return d_a
    else:
        return LeastCommMultip(d_b, d_a % d_b)


def ReduceFraction(d_n, d_m):
    return d_n // LeastCommMultip(d_n, d_m), d_m // LeastCommMultip(d_n, d_m)


print(*ReduceFraction(n, m))
