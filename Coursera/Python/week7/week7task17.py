# week 7 task 17
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# gc73D/samoie-chastoie-slovo
"""
текст задания                                                 тут 79 символ=>!
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.
Формат ввода - Вводится текст.
Формат вывода - Выведите ответ на задачу.
"""
fileIn = open('input.txt', 'r', encoding='utf8')
wordDict = {}
for line in fileIn:
    readLine = line.split()
    for j in readLine:
        wordDict[j] = wordDict.get(j, 0) + 1
fileIn.close()
print(sorted(wordDict.items(), key=lambda x: (-x[1], x[0]))[0][0])
