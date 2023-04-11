#!/usr/bin/python3

def get_products(a=1, b=9, c=1, d=9):
    res = []
    for i in range(a, b+1):
        for j in range(c, d+1):
            res.append(i * j)
    return res

print(get_products(1,2,1,4))