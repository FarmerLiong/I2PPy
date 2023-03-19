#!/usr/bin/python3 

str = input()
length = len(str)
if(length % 2 == 1) :
    str = str.capitalize()
    print(str[::-1])
else:
    print(str[:int(length/2 - 1)] + '42' + str[int(length/2 + 1):])
    