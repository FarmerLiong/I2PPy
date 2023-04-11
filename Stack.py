#!/usr/bin/python3

def init():
    global stack, squareSum
    stack = []
    squareSum = 0
    return None

def push(val):
    global stack, squareSum
    squareSum += val * val
    stack.append(val)
    return None

def pop():
    global stack, squareSum
    top = stack[-1]
    squareSum -= top * top
    stack.pop()
    return None

def top():
    return stack[-1]

def getSquareSum():
        return squareSum