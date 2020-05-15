# week 7 task 9
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# 53SZY/polighloty
"""
текст задания                                                 тут 79 символ=>!
Каждый из N школьников некоторой школы знает Mᵢ языков. Определите,
какие языки знают все школьники и языки, которые знает
хотя бы один из школьников.
Формат ввода - Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих
названия языков, которые знает i-й школьник. Длина названий языков не
превышает 1000 символов, количество различных языков не более 1000.
1≤N≤1000, 1≤Mᵢ≤500.
Формат вывода - В первой строке выведите количество языков, которые знают
все школьники. Начиная со второй строки - список таких языков. Затем -
количество языков, которые знает хотя бы один школьник, на следующих строках
- список таких языков.
"""

studentNum = int(input())  # количество школьников
languageOneKnowSet = set()
languageAllKnowSet = set()
for i in range(studentNum):
    languageNum = int(input())
    tempLanguageLeastOneSet = set()
    for j in range(languageNum):
        tempSet = input()
        languageOneKnowSet |= {tempSet}
        tempLanguageLeastOneSet |= {tempSet}
    if i == 0:
        languageAllKnowSet |= tempLanguageLeastOneSet
    else:
        languageAllKnowSet &= tempLanguageLeastOneSet

print(len(languageAllKnowSet))
for element in languageAllKnowSet:
    print(element)
print(len(languageOneKnowSet))
for element in languageOneKnowSet:
    print(element)
