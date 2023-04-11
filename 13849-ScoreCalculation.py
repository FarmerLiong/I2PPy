#!/usr/bin/python3 
import re

while True:
  try:
    _input = input()
    inputList = re.split(r',|/', _input)
    for i in range(len(inputList)):
        if i == 0:
           continue
        else:
           inputList[i] = float(inputList[i])
    print(f"Student_Name:{inputList[0]},Final_Score:{round(inputList[1]/inputList[2]*40, 2) + round(inputList[3]/inputList[4]*60, 2) + inputList[5]:.02f}")
  except EOFError as e:
    break