#!/usr/bin/python3
"""report balance after input initial amount of money and expenses record"""

balance = int(input("How much money do you have? "))
expensesRec = input("Add an expense or income record with description and amount:\n")

expensesList = expensesRec.split()
expenses  = int(expensesList[1])

balance += expenses

print("Now you have %d dollars.\n" % (balance))