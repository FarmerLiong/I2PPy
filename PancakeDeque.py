#!/usr/bin/python3 

for t in range(int(input())):
    length = int(input())
    cake = list(map(int, input().split()))
    Dmax = 0
    count = 0
    while length > 0:
        
        if cake[0] >= Dmax and cake[length-1] >= Dmax:
            if cake[0] < cake[length-1]:
                idx = 0
            else:
                idx = length - 1
            
        elif cake[0] >= Dmax:
            idx = 0
        elif cake[length-1] >= Dmax:
            idx = length - 1
        else:
            cake.pop(0)
            length -= 1
            if length > 0 : 
                cake.pop(length-1)
                length -= 1
            continue
        
        Dmax = cake[idx]
        cake.pop(idx)
        length -= 1
        count +=1
    print(f"Case #{t+1}: {count}")