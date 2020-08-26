# week 7 task 4
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# URmWN/vstriechalos-li-chislo-ran-shie
"""
текст задания                                                 тут 79 символ=>!
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число
ранее встречалось в последовательности или NO, если не встречалось.
Формат ввода - Вводится список чисел. Все числа списка находятся
на одной строке.
Формат вывода - Выведите ответ на задачу.
"""
stringIn = input().split()
lenStringIn = len(stringIn)
print('NO')
set1 = {stringIn[0]}
if lenStringIn > 1:
    for s in stringIn[1:]:
        if set1 >= {str(s)}:
            print('YES')
        else:
            print('NO')
        set1.add(str(s))
