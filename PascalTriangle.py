#!/usr/bin/python3

def pascal(row, col):
    return 1 if col == 0 or col == row else pascal(row-1, col-1) + pascal(row-1, col)

def print_pascal(n):
    for i in range(0, n):
        for j in range(i+1):
            print(f'{pascal(i, j):3d}', end='')
        print('')

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print_pascal(n)