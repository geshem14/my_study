# week 3 task 15
"""
текст задания
Дана строка. Если в этой строке буква f встречается только один раз,
выведите её индекс. Если она встречается два и более раз,
выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите.
При решении этой задачи нельзя использовать метод count и циклы.
"""
string = input()  # строковая переменная для ввода
search_string = "f"  # искомая строка
temp_position = string.find(search_string)  # врем. строка для позиции входа
position1 = temp_position  # переменная для первой позиции входа
position_last = -2  # переменная для последней позиции входа
while temp_position != -1:
    position_last = temp_position
    temp_position = string.find(search_string, temp_position + 1)
if position_last > position1:
    print(position1, position_last)
elif position1 >= 0:
    print(position1)
