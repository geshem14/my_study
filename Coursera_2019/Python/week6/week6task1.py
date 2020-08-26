# week 6 task 1
"""
текст задания                                                 тут 79 символ=>!
Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С
(то есть он должен содержать len(A)+len(B) элементов).
Решение оформите в виде функции merge(A, B), возвращающей новый список.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.
Формат ввода - Программа получает на вход два неубывающих списка,
каждый в отдельной строке.
Формат вывода - Программа должна вывести последовательность неубывающих чисел,
полученных объединением двух данных списков.
"""


def merge(d_List1, d_List2):
    newList = []
    lenList1 = len(d_List1)
    lenList2 = len(d_List2)
    i = 0
    j = 0
    while i < lenList1 and j < lenList2:
        if d_List1[i] < d_List2[j]:
            newList.append(d_List1[i])
            i += 1
        else:
            newList.append(d_List2[j])
            j += 1
    if j == lenList2:
        for temp_i in range(i, lenList1):
            newList.append(d_List1[temp_i])
    if i == lenList1:
        for temp_j in range(j, lenList2):
            newList.append(d_List2[temp_j])
    return newList


numList1 = list(map(int, input().split()))  # список1 для ввода
numList2 = list(map(int, input().split()))  # список2 для ввода
print(*merge(numList1, numList2))
