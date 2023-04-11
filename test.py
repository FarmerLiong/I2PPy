#!/usr/bin/python3

def genIntList(low, high, skip, exclude):
    myList = []
    for value in range(low, high, skip):
        if((value%exclude) != 0):
            myList.append(value)
    return myList

_list = genIntList(0,100,2,4)
print(_list)
# skip = 2
# boundary = [0,100]
# myList = []
# for value in range(boundary[0], boundary[1], skip):
#     if((value%4) != 0):
#         myList.append(value)
# print(myList)
