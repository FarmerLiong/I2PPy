#!/usr/bin/python3

inputList = [int(num) for num in input().split()]
print(f'Monday:{inputList[0]*2 + inputList[2]*3}')

inputList = [int(num) for num in input().split()]
print(f'Tuesday:{round(inputList[0]*0.2 + inputList[2]*5 + 20)}')

inputList = [int(num) for num in input().split()]
print(f'Wednesday:{round(inputList[0]*0.5 + inputList[2]*4 + 10)}')

inputList = [int(num) for num in input().split()]
print(f'Thursday:{round(inputList[0]*0.35 + inputList[2]*7 + 20)}')

inputList = [int(num) for num in input().split()]
print(f'Friday:{round(inputList[0]*0.2 + inputList[1]*5 + 100)}')

inputList = [int(num) for num in input().split()]
print(f'Sunday:{round(inputList[0]*0.8 + inputList[1]*15 + 105)}')
