# week 1 task 5
# https://www.coursera.org/learn/diving-in-python/programming/nxYyA/
# korni-kvadratnogho-uravnieniia
import sys
from math import sqrt


def SolutionReducedQEquation(d_b, d_c):
    """
    функция возвращает рещение приведенного квадратного уравнения
    d_a = 1
    d_b = b
    d_c = c * a
    """
    d_discriminant = d_b * d_b - 4 * d_c
    return -d_b + int(sqrt(d_discriminant)), -d_b - int(sqrt(d_discriminant))


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
# a = -1
# b = -1
# c = 20

solution1, solution2 = SolutionReducedQEquation(b, a * c)
if solution1 == solution2:
    print(solution1 // (2 * a))
else:
    print(solution1 // (2 * a))
    print(solution2 // (2 * a))
