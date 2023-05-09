#!/usr/bin/python3

inputList = input().split()
unwanted = input().split()

for u in unwanted:
    while u in inputList:
        del(inputList[inputList.index(u)])

print(' '.join(inputList))