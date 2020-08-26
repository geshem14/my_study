# week 6 task 12
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/
# programming/0WHfG/riezul-taty-olimpiady
"""
текст задания                                                 тут 79 символ=>!
В олимпиаде участвовало N человек. Каждый получил определенное количество
баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов.
Формат ввода - Программа получает на вход число участников олимпиады N.
Далее идет N строк, в каждой строке записана фамилия участника, затем,
через пробел, набранное им количество баллов.
Формат вывода - Выведите список участников (только фамилии) в порядке
убывания набранных баллов.
"""
N = int(input())
studentList = []
for i in range(N):
    student = input().split()
    studentList.append((student[0], int(student[1])))

studentList.sort(key=lambda x: -x[1])
for i in range(N):
    print(studentList[i][0])
