# week 5 task 14
"""
текст задания                                                 тут 79 символ=>!
Выведите все четные элементы списка.
Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
Формат вывода - Выведите ответ на задачу.
"""


def IsEvenNum(a):
    if int(a) % 2 == 0:
        return int(a)
    else:
        return " "


numList = list(map(IsEvenNum, input().split()))  # список для ввода
numList_str = ''.join(map(str, numList))
numList_evenElements = list(map(int, numList_str.split()))
print(*numList_evenElements)
