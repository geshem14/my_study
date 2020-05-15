# week 7 task 14
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# COVcr/nomier-poiavlieniia-slova
"""
текст задания                                                 тут 79 символ=>!
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось
в этом тексте ранее.
"""

fileIn = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
wordDict = {}

for line in fileIn:
    readLine = line.split()
    for j in readLine:
        wordDict[j] = wordDict.get(j, 0) + 1
        print(wordDict[j] - 1, end=" ", file=fileOut)
fileIn.close()
fileOut.close()
