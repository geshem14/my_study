# week 7 task 6
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# s9LoW/kolichiestvo-slov-v-tiekstie
"""
текст задания                                                 тут 79 символ=>!
Во входном файле (вы можете читать данные из sys.stdin,
подключив библиотеку sys) записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""
fileIn = open('input.txt', 'r', encoding='utf8')
wordList = []
for line in fileIn:
    wordList += line.split()

fileIn.close()
print(len(set(wordList)))
