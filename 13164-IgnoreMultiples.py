#!/usr/bin/python3

def genIntList(lower, upper, a, b):
    tmp = []
    for i in range(lower, upper):
        if i % a == 0 or i % b == 0:
            pass
        else:
            tmp.append(i)    
    return tmp

inputList = [int(num) for num in input().split(',')]
res = genIntList(inputList[0], inputList[1], inputList[2], inputList[3])

for idx, ans in enumerate(res):
    if(idx < len(res) - 1):
        print(f"{ans},", end='')   
    else:
        print(ans) 

        