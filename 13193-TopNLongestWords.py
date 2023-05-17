#!/usr/bin/python3

n = int(input())
strList = []
while True:
    try:
        inList = input().split()
        for i in inList:
            if i.isalpha():
                strList.append(i)
    except EOFError:
        break

strList.sort(key = lambda s : (len(s), sum([ord(c) for c in s])), reverse = True)
for s in strList:
    if n == 0:
        break
    print(s)
    n -= 1
