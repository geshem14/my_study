# week 3 task 2
"""
текст задания
По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
Вводится целое положительное число
"""
import math

n = int(input())  # переменная для вводимого числа
sum_of_squares = 1.0  # вспомогательная переменная для суммы квадратов
i = 2  # индекс для оператора while
while i <= n:
    sum_of_squares = sum_of_squares + 1 / (i * i)
    i = i + 1
"""
на последнем шаге сравниваем полученное число суммы
с окруленным числом и если разница между ними меньше
погрешности, тогда выводим результат с нужной погрешностью
"""
if abs(math.ceil(sum_of_squares)-sum_of_squares) < 10 ** -6:
    print(math.ceil(sum_of_squares))
elif abs(math.ceil(sum_of_squares*10)-sum_of_squares*10) < 10 ** -5:
    print('{0:.1f}'.format(sum_of_squares))
elif abs(math.ceil(sum_of_squares*100)-sum_of_squares*100) < 10 ** -4:
    print('{0:.2f}'.format(sum_of_squares))
else:
    print('{0:.6f}'.format(sum_of_squares))
