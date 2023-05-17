#!/usr/bin/python3

def Geometric_Sequence(first,common_ratio):
    cur = first % 100
    yield cur
    while True:
        cur *= common_ratio
        cur %= 100
        yield cur

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for i in range(1,T+1):
    n,f,cr = list(map(int,input().split()))
    g = Geometric_Sequence(f,cr)
    for j in range(n):
        print(f"Case #{i}_{j}: {next(g)}")