# week 3 task 10
"""
текст задания
Даны действительные коэффициенты a, b, c, при этом a != 0.
Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
Формат ввода
Вводятся три действительных числа.
Формат вывода
Если уравнение имеет два корня, выведите два корня в порядке
возрастания, если один корень — выведите одно число,
если нет корней — не выводите ничего.
"""
from math import ceil, sqrt

a, b, c = float(input()), float(input()), float(input())
# вещественные переменные для вводимых чисел
epsilon = 10 ** (-9)  # переменная для заданной точности

diskriminant = b * b - 4 * a * c
if diskriminant - epsilon > 0:  # если дискриминант больше нуля
    root_of_equation1 = ((-1) * b + sqrt(diskriminant)) / (2 * a)
    # вещ. переменная для первого корня уравнения
    root_of_equation2 = ((-1) * b - sqrt(diskriminant)) / (2 * a)
    # вещ. переменная для второго корня уравнения

    if root_of_equation1 > root_of_equation2:
        temp = root_of_equation2
        root_of_equation2 = root_of_equation1
        root_of_equation1 = temp

    a = root_of_equation1
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

    a = root_of_equation2
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


elif abs(diskriminant) < epsilon:  # если дискриминант равен нулю
    root_of_equation = ((-1) * b) / (2 * a)
    # вещ. переменная для первого корня уравнения

    a = root_of_equation
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
