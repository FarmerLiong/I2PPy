#!/usr/bin/python3 

T = int(input())
for i in range(T):
    numCandies = input().split()
    print(f"Case #{i+1}: {min(len(numCandies) // 2, len(set(numCandies)))}")
    