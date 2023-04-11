#!/usr/bin/python3 

t = int(input())
for i in range(t):
    str = input().split()
    if(list(reversed(str)) == str):
        print(f"Case #{i+1}: Yes")
    else:
        print(f"Case #{i+1}: No")
        