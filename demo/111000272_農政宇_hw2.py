#!/usr/bin/python3
import sys

# function definitions
def init():
    # declaration of variables for returning to initailAmount and ExpensesList
    expsList = []   
    initAmt = None

    # try open existing records.txt file 
    try:
        fh = open("records.txt", 'r')
        # read first line of file
        line = fh.readline()
        if line == '':                                      # dealing with no line in file problem
            sys.stderr.write("No line is found in the file. Initializing...\n")
            raise FileNotFoundError                         
        else:
            try:
                # split first line for read in initial_amount
                tmpList = line.split()
                try:
                    initAmtStr = tmpList[0]                 # check whether "initial_amount" name exists
                    if tmpList[0] == "initial_amount":      
                        initAmt = int(line.split()[1])      # read in initialAmount
                        inputList = fh.readlines()          # read the records in the rest of lines.
                        for records in inputList: 
                            tmpList = records.split()
                            if(len(tmpList) == 2):                     
                                intTest = int(tmpList[1])           # check validity of amount in records
                                expsList.append(tuple(tmpList))     # append records to expsList as tuple
                            else:
                                raise ValueError
                        print("Welcome back! ^^")
                    else:                                   # dealing with "initial_amount" name not found
                        sys.stderr.write("Initial amount not found. Initializing...\n")
                        raise FileNotFoundError
                except IndexError:                          # dealing with file with only '\n'
                    sys.stderr.write("Initial amount not found. Initializing...\n")
                    raise FileNotFoundError
            except ValueError:                              # dealing with invalid amount in records
                sys.stderr.write("Invalid amount format in the file. Initializing...\n")
                raise FileNotFoundError
            finally:
                # close file whether error occurs or not
                fh.close()

    # re-initializing while FileNotFoundError or other errors in reading file raised
    except FileNotFoundError:
        # reset initAmt and expsList while errors occur in reading file
        initAmt = None
        expsList = []   
        while initAmt is None:
            # prompt user for input of balance for initialization till initAmt successfully read in
            try:
                initAmt = int(input("How much money do you have? "))
            except ValueError:
                sys.stderr.write("Invalid format of amount. Try again.\n")
    
    # return to update initialAmount and ExpensesList after initializing
    return initAmt, expsList

def add(expsList):
    # prompt for input of addition of records
    inputStr = input("Add an expense or income record with description and amount:\n(eg: breakfast -50) ")
    
    # split input string
    inputList = inputStr.split()
    if len(inputList) == 2:                                 # check validity of input         
        try:
            intTest = int(inputList[1])                     # check format of amount
            expsList.append((inputList[0], inputList[1]))   # append record to expensesList as tuple
        except ValueError:                                  # dealing with invalid format of amount
            sys.stderr.write("Invalid format for amount\n") 
    else:                                                   # dealing with invalid format of input
        sys.stderr.write("Invalid format of input.('items' 'amt')\n")
    # return to update modified expensesList
    return expsList

def view(initAmt, expsList):
    # calculate balance and output records
    
    print("Here's your expense and income records:\nItems                 Amount\n--------------------  ------")
    # enumerate to show index of records 
    for idx, records in enumerate(expsList):                
            print(f"{idx + 1}: {records[0]:<18s} {records[1]:>6s}")
    print("--------------------  ------")
    balance = initAmt + sum([int(records[1]) for records in expsList])
    print(f"Now you have {balance} dollars.\n")
    return None

def delete(expsList):
    # show current records for sack of user
    if len(expsList) == 0:
        sys.stderr.write("No record available to be removed\n")
    else:
        print("Current records:\nItems                 Amount\n--------------------  ------")
        for idx, records in enumerate(expsList):
                print(f"{idx + 1}: {records[0]:<18s} {records[1]:>6s}")
        print("--------------------  ------")
        try:
            # prompt for index of item to delete
            idxDel = int(input("Which record do you want to delete?(eg: 2 #to delete item with index 2) "))
            if idxDel - 1 < 0:                                  # dealing with out of index problem
                raise IndexError
            else:
                del(expsList[idxDel - 1])                       # delete selected record
        except ValueError:                                      # dealing with invalid format of input
            sys.stderr.write("Invalid format. Try again.\n")
        except IndexError:                                      
            sys.stderr.write("Out of index. Try again.\n")
        # return to update modified expensesList
    return expsList         

def save(initAmt, expsList):
    # open records.txt and write in initialAmount and ExpensesList of current program
    with open("records.txt", 'w') as fh:
        # write initial_amount as first line
        fh.write(f"initial_amount {initAmt}\n")
        # create str list of records and write expensesList for the rest of lines
        recordsList = [" ".join([records[0], records[1]]) + '\n' for records in expsList]
        fh.writelines(recordsList)
    return None

# start main program
initialAmount, expensesList = init()
while True:
    # prompt user for input of command
    command = input("\nWhat do you want to do (add / view / delete / exit)? ")
    
    if command == "add":                #dealing "add" command
        expensesList = add(expensesList)

    elif command == "view":             #dealing "view" command
        view(initialAmount, expensesList)

    elif command == "delete":           #dealing "delete" command
        expensesList = delete(expensesList)

    elif command == "exit":             #dealing "exit" command
        save(initialAmount, expensesList)
        break

    else:                               #dealing invalid command
        sys.stderr.write("Invalid command. Try again.\n")


