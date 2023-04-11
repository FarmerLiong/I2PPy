#!/usr/bin/python3 

for t in range(int(input())):
    res = 0
    L = list(map(int, input().split()))
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                res += 1
    print(f"Case #{t+1}: {res}")
