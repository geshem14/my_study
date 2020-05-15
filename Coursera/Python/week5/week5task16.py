# week 5 task 16
"""
текст задания                                                 тут 79 символ=>!
Найдите наибольшее значение в списке и индекс последнего элемента,
который имеет данное значение за один проход по списку,
не модифицируя этот список и не используя дополнительного списка.
Выведите два значения.
"""


def MaxInList_and_IndexLastMax(a):
    """
    функция возвращает значения максимум и индекс последн. максимума в списке
    :param a: список
    :return: два значения максимум и индекс последнего максимума
    """
    temp_max = -10 ** 9
    index_last_max = 0
    for i in range(0, len(a)):
        temp = a[i]
        if temp > temp_max:
            temp_max = temp
        if temp == temp_max:
            index_last_max = i
    return temp_max, index_last_max


numList = list(map(int, input().split()))  # список для ввода
print(*MaxInList_and_IndexLastMax(numList))
