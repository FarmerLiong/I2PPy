#!/usr/bin/python3

total = 0
inputList = []
cheat = []
records = []
weightList = [float(weight) for weight in input().split()]
while True:
    try:
        inputList.append(input())
    except EOFError as e:
        break

listLen = len(inputList)

for s in inputList:
    if s[0] == 'X':
        cheat.append(s[1:])
    else:
        records.append(s.split(','))

for i, record in enumerate(records):
    scores = 0
    flag = []
    for check in record[:1:-1]:
        if check[0] == 'd':
            flag.append(int(check[1:]))
        else:
            total = check
            break
    for j, score in enumerate(record[2:]):
        if score == total:
            break
        elif j+1 in flag:
            pass
        else:
            scores += eval(score) * weightList[j]
    for check in cheat:
        length = len(check)
        if check == record[1][-length:]:
            scores = 0.00
    scores = scores / sum(weightList) *100
    print(f'{record[1]},{scores:.02f}')
  
       