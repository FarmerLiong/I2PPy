#!/usr/bin/python3

def reverse(L):
    if type(L) in {list, tuple}:
        retl = list(L[::-1])
        # print(retl)
        for i, e in enumerate(retl):
            retl[i] = reverse(e)
        return retl
    else:
        return L

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    L = eval(input())
    rL = reverse(L)
    print(L)
    print(rL)