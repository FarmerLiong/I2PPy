#!/usr/bin/python3

res = []
seq = [int(x) for x in input().split()]
sec = input()
seq.sort()

for idx in seq:
    if sec[idx-1] == '*':
        res.append(' ')
    else:
        c = sec[idx-1]
        c = c.upper()
        res.append(c)

print(''.join(res))
