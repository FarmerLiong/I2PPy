#!/usr/bin/python3

res = {}

while True:
    try:
        inList = input().split()
        name = inList[0].lower()
        if name in res:
            if inList[1] == 'I':
                res[name] += int(inList[2])
            elif inList[1] == 'O':
                res[name] -= int(inList[2])
        else:
            res[name] = 0
            if inList[1] == 'I':
                res[name] += int(inList[2])
            elif inList[1] == 'O':
                res[name] -= int(inList[2])
    except EOFError:
        break

for item in res:
    print(f'{item} {res[item]}')