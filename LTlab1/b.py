#!/usr/bin/python3

mulp = [1,9,8,7,6,5,4,3,2,1,1]
id = []
inputList = []
res = 0
while True:
    try:
        s = input()
        if s.isdigit():
            id = [int(d) for d in s]
        else:
            inputList.append(s)
    except EOFError as e:
        break

for i, d in enumerate(id):
    res += d * mulp[i+2]

citiesList = [city.split(',') for city in inputList]

for city in citiesList:
    sum = res + int(city[1][0]) * mulp[0] + int(city[1][1]) * mulp[1]
    if sum % 10 == 0:
        print(city[2])
        break

