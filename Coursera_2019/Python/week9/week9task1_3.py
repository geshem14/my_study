from sys import stdin
from copy import deepcopy

# week 9 task 3
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# 9Vl6a/oshibki-transponirovaniie
# last task in course


class MatrixError(BaseException):
    def __init__(self, c_matrix1, c_matrix2):
        self.matrix1 = c_matrix1
        self.matrix2 = c_matrix2


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
            c_temp_add = []
            for i in range(len(self.matrix)):
                c_temp_add2 = []
                for j in range(len(self.matrix[0])):
                    d = self.matrix[i][j] + other.matrix[i][j]
                    c_temp_add2.append(d)
                c_temp_add.append(c_temp_add2)
            return Matrix(c_temp_add)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        c_temp_add = deepcopy(self)
        i = 0
        for row in self.matrix:
            for j in range(len(row)):
                c_temp_add.matrix[i][j] = c_temp_add.matrix[i][j] * other
            i += 1
        return c_temp_add

    __rmul__ = __mul__

    def transpose(self):
        c_temp_tr = list(zip(*self.matrix))
        self.matrix = c_temp_tr
        return Matrix(c_temp_tr)

    def transposed(self):
        c_temp_tr = list(zip(*self.matrix))
        return Matrix(c_temp_tr)


exec(stdin.read())
