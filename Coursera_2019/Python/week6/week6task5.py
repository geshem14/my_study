# week 6 task 5
"""
текст задания                                                 тут 79 символ=>!
Системный администратор вспомнил, что давно не делал архива пользовательских
файлов. Однако, объем диска, куда он может поместить архив, может быть меньше
чем суммарный объем архивируемых файлов.
Известно, какой объем занимают файлы каждого пользователя.
Напишите программу, которая по заданной информации о пользователях и
свободному объему на архивном диске определит максимальное число пользователей
, чьи данные можно поместить в архив.
Формат ввода - Программа получает на вход в одной строке число S – размер
свободного места на диске (натуральное, не превышает 10000), и число N
– количество пользователей (натуральное, не превышает 100), после этого
идет N чисел - объем данных каждого пользователя (натуральное,
не превышает 1000), записанных каждое в отдельной строке.
Формат вывода - Выведите наибольшее количество пользователей, чьи данные
могут быть помешены в архив.
"""


def rec(N):
    d_newList = []
    for n in range(1, N+1):
        n = int(input())
        d_newList.append(n)
    return d_newList


numList = list(map(int, input().split()))  # список1 для ввода
S = numList[0]
N = numList[1]
newList = rec(N)

lenList = len(newList)  # константа длины списка
newList.sort()  # сортировка списка
temp_sum = newList[0]
i = 1
index = 0
if temp_sum < S:
    while i < lenList:
        temp_sum += newList[i]
        if temp_sum > S:
            index = i
            i = lenList
        else:
            i += 1
    if i >= lenList and index == 0:
        index = lenList

print(index)
