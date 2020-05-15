# week 7 task 4 test
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


def test(d_stringIn):
    # stringIn = input().split()
    stringIn = d_stringIn

    lenStringIn = len(stringIn)
    print('NO', end=" ")
    set1 = {stringIn[0]}
    if lenStringIn > 1:
        for s in stringIn[1:]:
            set2 = {str(s)}
            if set1 >= set2:
                print('YES', end=" ")
            else:
                print('NO', end=" ")
            set1.add(str(s))
        print()

'''
print("test1")
str1 = "1"
print(str1)
test(str1.split())
print("NO")
print()

print("test2")
str1 = "1 1"
print(str1)
test(str1.split())
print("NO YES")
print()

print("test3")
str1 = "1 1 1"
print(str1)
test(str1.split())
print("NO YES YES")
print()

print("test4")
str1 = "1 1 2"
print(str1)
test(str1.split())
print("NO YES NO")
print()

print("test5")
str1 = "1 1 2 1"
print(str1)
test(str1.split())
print("NO YES NO YES")
print()
'''
print("test6")
str1 = "10000000 1000000 2 1000000"
print(str1)
test(str1.split())
print("NO NO NO YES")
print()
