# week 5 task 31
"""
текст задания                                                 тут 79 символ=>!
Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
Формат ввода - Вводится список чисел. Все числа списка находятся
на одной строке.
"""

numList = list(map(int, input().split()))  # список для ввода
tempList = []  # временный список для вывода
i = 0
lenList = len(numList)
while i < lenList - 1:
    tempList.append(numList[i + 1])
    tempList.append(numList[i])
    i += 2
if lenList % 2 != 0:
    tempList.append(numList[lenList - 1])
print(*tempList)
