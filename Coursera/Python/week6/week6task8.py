# week 6 task 8
# https://www.coursera.org/learn/python-osnovy-programmirovaniya
# /programming/OE01R/otsortirovat-spisok-uchastnikov-po-alfavitu
"""
текст задания                                                 тут 79 символ=>!
Известно, что фамилии всех участников — различны. Сохраните в массивах список
всех участников и выведите его, отсортировав по фамилии в лексикографическом
порядке. При выводе указываете фамилию, имя участника и его балл.
Используйте для ввода и вывода файлы input.txt и output.txt с указанием
кодировки utf8. Например, для чтения откройте файл с помощью
open('input.txt', 'r', encoding='utf8').
Входные данные - Строки вида "Фамилия Имя НомерШколы Балл".
Выходные данные - Строки вида "Фамилия Имя Балл", отсортированные по фамилии.
Примечание - Если у Вас Wrong Answer на первом тесте и в вердикте
в качестве правильного ответа показываются знаки вопросов, это не значит,
что их действительно нужно выводить. Это баг Курсеры – в вердикте кириллица
не поддерживается. Курсера знает о проблеме с 25.10.2018 и возможно починит.
В итоге, при WA на первом тесте не стоит смотреть на вердикт, нужно искать
ошибку в решении.
"""

fileIn = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
studentsList = []
for student in fileIn.readlines():
    if list(student.split()):
        studentsList.append([list(student.split())[0],
                             list(student.split())[1],
                             list(student.split())[3], ])

studentsList.sort(key=lambda x: x[0])

for student in studentsList:
    rec = [student[0], student[1], student[-1]]
    print(*rec, file=fileOut)

fileOut.close()
