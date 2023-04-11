#!/usr/bin/python3 

for t in range(int(input())):
    str = input()
    pos = int(input())
    if pos == 0:
        print(f"Case #{t+1}: {str}")
    else:
        pos %= len(str)
        print(f"Case #{t+1}: {str[pos:] + str[:pos]}")