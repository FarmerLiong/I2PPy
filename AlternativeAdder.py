#!/usr/bin/python3 

def adder(*list):
    res = 0
    res += sum(list[0::2])
    res -= sum(list[1::2])
    return res

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        args = map(int, input().split())
        print("Case #%d: %d" % (i, adder(*args)))