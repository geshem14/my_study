# week 7 task 15
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# H68aa/slovar-sinonimov
"""
текст задания                                                 тут 79 символ=>!
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом
к парному ему слову. Все слова в словаре различны. Для одного данного слова
определите его синоним.
Формат ввода - Программа получает на вход количество пар синонимов N.
Далее следует N строк, каждая строка содержит ровно два слова-синонима.
После этого следует одно слово.
Формат вывода - Программа должна вывести синоним к данному слову.
"""

fileIn = open('input.txt', 'r', encoding='utf8')
N = int(fileIn.readline())
synonymDict = {}
for i in range(N):
    readLine = fileIn.readline().split()
    synonymDict[readLine[0]] = readLine[1]
    if readLine[0] != readLine[1]:
        synonymDict[readLine[1]] = readLine[0]
print(synonymDict[fileIn.readline().strip()])
fileIn.close()
