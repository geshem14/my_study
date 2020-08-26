from sys import stdin
from copy import deepcopy
# week 9 task 1
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
# albda/klass


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


exec(stdin.read())
