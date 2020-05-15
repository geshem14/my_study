# week 4 task 18
"""
текст задания                                                 тут 79 символ=>!
Дана последовательность чисел, завершающаяся числом 0.
Найдите сумму всех этих чисел, не используя цикл.
Формат ввода
Вводится последовательность целых чисел,
оканчивающаяся числом 0 (само число 0 в последовательность не входит,
а служит как признак ее окончания).
"""

temp_sum_global = 0


def SummElementOfSequence():
    global temp_sum_global
    n = int(input())
    temp_sum_global += n
    if n != 0:
        SummElementOfSequence()
        return


SummElementOfSequence()
print(temp_sum_global)
