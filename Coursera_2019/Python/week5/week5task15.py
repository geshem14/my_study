# week 5 task 15
"""
текст задания                                                 тут 79 символ=>!
Найдите количество положительных элементов в данном списке.
Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
Формат вывода - Выведите ответ на задачу.
"""


def IsPositiveNum(a):
    if int(a) > 0:
        return 1
    else:
        return ''


numList = list(map(IsPositiveNum, input().split()))  # список для ввода
numList_str = ''.join(map(str, numList))  # строка единиц по кол-ву положит.ых
print(len(numList_str))
