#!/usr/bin/python3

from itertools import combinations

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    binaries = [2**i for i in range(n)]
    res = list(map(sum, combinations(binaries, k)))
    print(f'Case #{t+1}: {sorted(res)}')
