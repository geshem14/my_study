# week 2 task 31
"""
текст задания
Последовательность состоит из целых чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит,
а служит как признак ее окончания).
"""
bool_step = True  # вспом. логическая переменная для разршения след шага
max_element = 0  # переменная для наибольшего элемента последовательности
while bool_step:
    i = int(input())  # вспом. переменная для вводимого числа послед-ости
    if i > max_element:
        max_element = i
    elif i == 0:
        bool_step = False
print(max_element)
