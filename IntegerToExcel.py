#!/usr/bin/python3 

for t in range(int(input())):
    res = []
    num = int(input())
    while(num > 0):
        num -= 1 # 0-based
        res.insert(0, chr(ord('A') + num % 26))
        num //= 26
    print(f"Case #{t+1}: {''.join(res)}")



        