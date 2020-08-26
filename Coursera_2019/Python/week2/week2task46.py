# week 2 task 46
"""
текст задания
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой
последовательности равны друг другу.
Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит,
а служит как признак ее окончания).
"""
bool_step = True  # вспом. логическая переменная для разршения след шага
length_of_sequence = 1  # вспом. переменная для длины посл-ти
max_length_of_sequence = 0  # вспом. переменная для максим. длины посл-ти
previous_element_of_sequence = 0  # переменная для кол-ва макс.эл-тов посл-ти
while bool_step:
    i = int(input())  # вспом. переменная для вводимого числа послед-ости
    if i == previous_element_of_sequence and i != 0:
        length_of_sequence = length_of_sequence + 1
    elif i != previous_element_of_sequence:
        if length_of_sequence > max_length_of_sequence:
            max_length_of_sequence = length_of_sequence
        length_of_sequence = 1
    if i == 0:
        bool_step = False
    previous_element_of_sequence = i
print(max_length_of_sequence)
