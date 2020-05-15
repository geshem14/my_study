# week 7 task 19
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# FdeT5/vybory-priezidienta
"""
текст задания                                                 тут 79 символ=>!
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
половины числа голосов избирателей. Если такого кандидата нет, то во второй
тур выборов выходят два кандидата, набравших наибольшее число голосов.
Формат ввода
Каждая строка входного файла содержит имя кандидата, за которого отдал голос
один избиратель. Известно, что общее число кандидатов не превосходит 20,
но в отличии от предыдущих задач список кандидатов явно не задан. Читайте
данные из файла input.txt с указанием кодировки utf8.
Формат вывода -Если есть кандидат, набравший более 50% голосов, программа
должна вывести его имя. Если такого кандидата нет, программа должна вывести
имя кандидата, занявшего первое место, затем имя кандидата, занявшего второе
место. Выводите данные в файл output.txt с указанием кодировки utf8.
"""
fileIn = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
string1 = fileIn.readline().strip()
candidateDict = {string1: 1}
sumOfVotes = 1
for line in fileIn:
    candidateDict[line.strip()] = candidateDict.get(line.strip(), 0) + 1
    sumOfVotes += 1
fileIn.close()
sortCandidateList = sorted(candidateDict.items(), key=lambda x: (-x[1], x[0]))
if sortCandidateList[0][1] * 2 > sumOfVotes:
    print(sortCandidateList[0][0], file=fileOut)
else:
    print(sortCandidateList[0][0], file=fileOut)
    print(sortCandidateList[1][0], file=fileOut)
