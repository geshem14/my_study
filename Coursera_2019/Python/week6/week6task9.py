# week 6 task 9
# https://www.coursera.org/learn/python-osnovy-programmirovaniya
# /programming/66PkM/sortirovka-podschietom
"""
текст задания                                                 тут 79 символ=>!
Дан список из N (N≤2*10⁵) элементов,
которые принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.
Решение оформите в виде функции CountSort(A), которая модифицирует
передаваемый ей список. Использовать встроенные функции сортировки нельзя.
"""


def CountSort(d_List):
    maxList = max(d_List)
    counterNum = [-1] * (maxList + 1)
    for num in d_List:
        counterNum[num] += 1

    for now in range(maxList + 1):
        if counterNum[now] > -1:
            print((str(now) + ' ') * (counterNum[now] + 1), end='')


numList = list(map(int, input().split()))  # список для ввода
lenList = len(numList)  # константа длины списка
CountSort(numList)
