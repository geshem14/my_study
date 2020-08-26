# week 7 task 3
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# MJXOK/pieriesiechieniie-mnozhiestv
"""
текст задания                                                 тут 79 символ=>!
Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
Выведите все числа, которые входят как в первый, так и во второй список,
в порядке возрастания.
Формат ввода - Вводятся два списка чисел. Все числа каждого списка находятся
на отдельной строке.
"""
print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))
