#!/usr/bin/python3
import operator as op

class Matrix:
    # size: a integer represented the size of the square matrix
    # m: the matrix represented in the 2-d list format
    # create a square matrix
    def __init__(self, size, m):
        self._size = size
        self._m = m

    # create a new Matrix with the value of current matrix + rhs matrix
    def __add__(self, rhs):
        m3 = []
        for i in range(self._size):
            m3.append(list(map(op.add, self._m[i], rhs._m[i])))
        return Matrix(self._size, m3)

    # create a new Matrix with the value of current matrix - rhs matrix
    def __sub__(self, rhs):
        m3 = []
        for i in range(self._size):
            m3.append(list(map(op.sub, self._m[i], rhs._m[i])))
        return Matrix(self._size, m3)

    # create a new Matrix with the value of current matrix * rhs matrix
    def __mul__(self, rhs):
        m3 = []
        for i in range(self._size):
            m3.append([])
            for j in range(self._size):
                m3[i].append(0)
                for k in range(self._size):
                    m3[i][j] += self._m[i][k] * rhs._m[k][j]
        return Matrix(self._size, m3)
                

    # output format of Matrix
    def __repr__(self):
        return '\n'.join([' '.join(map(str, self._m[i])) for i in range(self._size)])

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    k = int(input())
    m1_list = []
    for _ in range(k):
        m1_list.append(list(map(int, input().split())))

    m2_list = []
    for _ in range(k):
        m2_list.append(list(map(int, input().split())))

    m1 = Matrix(k, m1_list)
    m2 = Matrix(k, m2_list)
    print(m1+m2)
    print(m1-m2)
    print(m1*m2)