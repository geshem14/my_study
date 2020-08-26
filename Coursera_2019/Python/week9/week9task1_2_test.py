from sys import stdin
from copy import deepcopy


# week 9 task 2
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# cTJex/dobavit-umnozhit


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
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        size_self = Matrix.size(self)
        if size_self == Matrix.size(other):
            c_temp_add = deepcopy(self)
            i = 0
            for row in other.matrix:
                for j in range(size_self[1]):
                    c_temp_add.matrix[i][j] = c_temp_add.matrix[i][j] + row[j]
                i += 1
        return c_temp_add

    def __mul__(self, other):
        c_temp_add = deepcopy(self)
        i = 0
        for row in self.matrix:
            for j in range(len(row)):
                c_temp_add.matrix[i][j] = c_temp_add.matrix[i][j] * other
            i += 1
        return c_temp_add

    __rmul__ = __mul__


# Task 2 check 1
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())

# Task 2 check 2
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

# Task 2 check 3
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)

exec(stdin.read())
