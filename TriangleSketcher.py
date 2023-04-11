#!/usr/bin/python3

def trisketch(n):
    for i in range(1, n+1):
        print('*' * i)


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    trisketch(n)