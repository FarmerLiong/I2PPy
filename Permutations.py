#!/usr/bin/python3

def permute(nums):
    if len(nums) == 1:
        return [nums]
    perm = []
    for lead in nums:
        tmp = permute([x for x in nums if x != lead])
        for subperm in tmp:
            perm.append([lead] + subperm)
    return perm

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    print(permute(nums))