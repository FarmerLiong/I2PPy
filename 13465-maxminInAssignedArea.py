#!/usr/bin/python3
number = []
num_list = []
indicators = []
findmax = -1

input_list = input().split(",")
#print(input_list)

for i in input_list:
    if i.isdigit(): ##如果i是數字
        i = int(i)
        number.append(i)
    elif i.startswith('i'):
        if i == "i1":
            findmax = 1
        elif i == "i2":
            findmax = 0
        indicators.append(i)
    elif i.startswith('f') or i.startswith('b'):
        indicators.append(i)

for i in indicators:
    if i.startswith('f'):
        k = int(i[1:])
        num_list = number[:k]
        if k == 0:
            print("None")
            exit()
        break
    elif i.startswith('b'):
        k = int(i[1:])
        num_list = number[-k:]
        if k == 0:
            print("None")
            exit()
        break

if num_list == []:
    num_list = number

if findmax == 1:
    print(max(num_list))
elif findmax == 0:
    print(min(num_list))
else:
    print("None")
    exit()