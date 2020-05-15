# week 5 task 33
"""
текст задания                                                 тут 79 символ=>!
В списке все элементы попарно различны. Поменяйте местами минимальный
и максимальный элемент этого списка.
Формат ввода - Вводится список целых чисел. Все числа списка находятся
на одной строке.
"""
numList = list(map(int, input().split()))  # список для ввода
temp_min = 10 ** 9  # временная переменная для минимума
temp_max = -10 ** 9  # временная переменная для максимума
index_max = -1  # переменная для индекса максимума
index_min = -1  # переменная для индекса минимума
lenList = len(numList)
for i in range(0, lenList):
    temp1 = numList[i]
    if temp1 < temp_min:
        temp_min = temp1
        index_min = i
    if temp1 > temp_max:
        temp_max = temp1
        index_max = i

for i in range(0, lenList):
    if i == index_max:
        numList[i] = temp_min
    if i == index_min:
        numList[i] = temp_max
print(*numList)
