# week 5 task 22
"""
текст задания                                                 тут 79 символ=>!
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент,
а значения всех элементов списка по модулю не превосходят 1000.
"""


def IsPositiveNum(a):
    d_temp = int(a)
    if d_temp > 0:
        return d_temp
    else:
        return 10000


numList = list(map(IsPositiveNum, input().split()))  # список для ввода
temp_min = 1000
for i in range(1, len(numList)):
    temp1 = numList[i]
    if temp1 < temp_min:
        temp_min = temp1

print(temp_min)
