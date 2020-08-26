# week 1 task 1
# https://d3c33hcgiwev3.cloudfront.net/
# _9db154b9cb5aaeacb9c3a1b69eed1482_01_primer_na_konstrukcii_upravleniya_
# potokom.slides.html?Expires=1572652800&Signature=LDd5OoFx-I7gEFNseZYVUQ410
# wutAEFV9pXNS428ztFqI2Kbpp39F80V5QHmUmKqBd6ojInSlOYsels~Yc2elwLaYqlPuhVBcR1V
# y~D91lx5PH83HJ~hiU53ENUNuqvoP56wjLBU-wNIVBzq90f5U058dmw3Fko6rsJ8k4knP5Q_
# &Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
"""
текст задания                                                 тут 79 символ=>!

"""
import random

x = 0
y = 12
name = x or y
print(name)


number = random.randint(0, 101)

while True:
    answer = input('Угадайте число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введите правильное число")
        continue

    answer = int(answer)

    if answer == number:
        print('Совершенно верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
