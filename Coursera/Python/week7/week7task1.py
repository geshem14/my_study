# week 7 task 1
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# gdjwh/kolichiestvo-razlichnykh-chisiel
"""
текст задания                                                 тут 79 символ=>!
Дан список чисел, который может содержать до 100000 чисел.Определите,
сколько в нем встречается различных чисел.
Формат ввода - Вводится список целых чисел. Все числа списка находятся
на одной строке.
"""
print(len(set(map(int, input().split()))))
