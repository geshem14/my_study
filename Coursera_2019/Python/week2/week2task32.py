# week 2 task 32
"""
текст задания
По данному натуральному n вычислите сумму 1²+2²+3²+...+n²
"""
n = int(input())  # переменная для вводимого числа
sum_of_squares = 1  # вспомогательная переменная для суммы квадратов
i = 2  # индекс для оператора while
while i <= n:
    sum_of_squares = sum_of_squares + i * i
    i = i + 1
print(sum_of_squares)
