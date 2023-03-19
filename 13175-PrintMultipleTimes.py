#!/usr/bin/python3 

list = input().split(',')
str = list[2] + list[1]
print(str * int(list[0]) + list[2])