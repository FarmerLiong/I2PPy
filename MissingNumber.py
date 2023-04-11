#!/usr/bin/python3 

for t in range(int(input())):
    nums = list(map(int, input().split()))
    maxN = max(nums)
    maxList = [i for i in range(maxN+1)]
    if set(nums) == set(maxList):
        print(f"Case #{t+1}: {maxN+1}")
    else:
        print(f"Case #{t+1}: {(set(nums) ^ set(maxList)).pop()}")
