#!/usr/bin/python3

inputList = []
scores = {}
while True:
    try:
        inputList = input().split()
        if inputList[0] in scores:
            scores[inputList[0]] +=  int(inputList[1])
        else:
            scores[inputList[0]] = int(inputList[1])
    except EOFError as e:
        break

for score in scores:
    print(f'{score} {scores[score]}')