from sys import stdin
from copy import deepcopy

# week 9 task 1
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# albda/klass
"""
текст задания                                                 тут 79 символ=>!
Реализуйте класс Matrix. Он должен содержать:
Конструктор от списка списков. Гарантируется, что списки состоят из чисел, 
не пусты и все имеют одинаковый размер. Конструктор должен копировать 
содержимое списка списков, т. е. при изменении списков, от которых была 
сконструирована матрица, содержимое матрицы изменяться не должно.
Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной 
строки должны быть разделены знаками табуляции, а строки — переносами строк. 
После каждой строки не должно быть символа табуляции и в конце не должно быть 
переноса строки.
Метод size без аргументов, возвращающий кортеж вида (число строк, число 
столбцов). 
"""


class Matrix:
    def __init__(self, listOfLists):
        self.matrix = deepcopy(listOfLists)

    def __str__(self):
        str1 = ''
        for row in self.matrix:
            str1 += '\t'.join(map(str, row))
            str1 += '\n'
        str1 = str1.rstrip('\n')
        return str1

    def size(self):
        sizepair = (len(self.matrix), len(self.matrix[0]))
        return sizepair


# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)

# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))

# Task 1 check 3
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m) == '1\t1\t1\n0\t100\t10')

exec(stdin.read())
