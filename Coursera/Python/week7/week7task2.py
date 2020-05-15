# week 7 task 2
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# ghZju/kolichiestvo-sovpadaiushchikh
"""
текст задания                                                 тут 79 символ=>!
Даны два списка чисел, которые могут содержать до 100000 чисел каждый.
Посчитайте, сколько чисел содержится одновременно как в первом списке,
так и во втором.
Формат ввода - Вводятся два списка чисел. Все числа каждого списка находятся
на отдельной строке.
"""
print(len(set(map(int, input().split())) & set(map(int, input().split()))))
