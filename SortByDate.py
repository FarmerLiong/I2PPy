#!/usr/bin/python3

def sort_by_date(L):
    L.sort(key = lambda d: (d[4:8], d[0:2], d[2:4]))
    return L

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    date_list = input().split()
    sort_by_date(date_list)
    print(date_list)