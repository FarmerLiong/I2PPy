#!/usr/bin/python3 

t = int(input())
for i in range(t):
    nums1 = set([int(num) for num in input().split()])
    nums2 = set([int(num) for num in input().split()])
    res = list(nums1 & nums2)
    print(f"Case #{i+1}: {sorted(res)}")