#!/usr/bin/python3
import sys
error_message = {
'NoLineInFile':
'No line is found in the file. Initializing...\n',

'InitialAmountNotFound':
'Initial amount not found. Initializing...\n',

'InvalidInitialAmountFormat':
'Invalid format of initial amount in the file. Initializing...\n',

'InvalidAmountFormat':
'Invalid format of amount. Try again.\n',

'InvalidFormat_ADD':
"Invalid format of input.('category' 'description' 'amt')\n",

'InvalidFormat_OTHERS':
'Invalid format. Try again.\n',

'OutOfIndex':
'Out of index. Try again.\n',

'CategoryNotFound_ADD' : 
'The specified category is not in the category list.\n\
You can check the category list by command "view categories".\n\
Fail to add a record.\n',

'CategoryNotFound_FIND' : 
'The specified category is not in the category list.\n\
You can check the category list by command "view categories".\n\
Fail to find records.\n',

'InvalidCommand':
'Invalid command. Try again.\n'
}

# class definitions
class Record:
    """Represent a record.\n
    Example usage:
    >>> record = Record('meal', 'breakfast', -50)
    >>> record.amount
    -50
    """
    def __init__(self, category, description, amount):
        """Constructor of class 'Records'"""        
        self._category = category
        self._description = description
        self._amount = amount

    @property
    def get_category(self):
        """getter method for category of record"""
        return self._category
    @property
    def get_description(self):
        """getter method for description of record"""
        return self._description
    @property
    def get_amount(self):
        """getter method for amount of record"""
        return self._amount
    
    def __repr__(self):
        return f'Record: {self._category} {self._description} {self._amount}'

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    
    def __init__(self):
        """Constructor of class 'Records'"""
        self._records = []
        self._initial_money = None
        try:
            fh = open("records.txt", 'r')
            # read first line of file
            line = fh.readline()
            if line == '':                                      # dealing with no line in file problem
                sys.stderr.write(error_message["NoLineInFile"])
                raise FileNotFoundError                         
            else:
                try:
                    # split first line for read in initial_amount
                    tmp_list = line.split()
                    try:
                        init_amt_str = tmp_list[0]                 # check whether "initial_amount" name exists
                        if init_amt_str == "initial_amount":      
                            self._initial_money = int(line.split()[1])      # read in initialAmount
                            input_list = fh.readlines()          # read the records in the rest of lines.
                            for records in input_list: 
                                tmp_list = records.split()
                                if(len(tmp_list) == 3):                     
                                    category = tmp_list[0]
                                    description = tmp_list[1]
                                    amount = int(tmp_list[2])           # check validity of amount in records
                                    self._records.append(Record(category, description, amount))     # append records to exps_list as tuple
                                else:
                                    raise ValueError
                            print("Welcome back! ^^")
                        else:                                   # dealing with "initial_amount" name not found
                            sys.stderr.write(error_message["InitialAmountNotFound"])
                            raise FileNotFoundError
                    except IndexError:                          # dealing with file with only '\n'
                        sys.stderr.write(error_message["InitialAmountNotFound"])
                        raise FileNotFoundError
                except ValueError:                              # dealing with invalid amount in records
                    sys.stderr.write(error_message["InvalidInitialAmountFormat"])
                    raise FileNotFoundError
                finally:
                    # close file whether error occurs or not
                    fh.close()

        # re-initializing while FileNotFoundError or other errors in reading file raised
        except FileNotFoundError:
            # reset self._initial_money and exps_list while errors occur in reading file
            self._records = []   
            self._initial_money = None
            while self._initial_money is None:
                # prompt user for input of balance for initialization till self._initial_money successfully read in
                try:
                    self._initial_money = int(input("How much money do you have? "))
                except ValueError:
                    sys.stderr.write(error_message["InvalidAmountFormat"])

    def add(self, input_str, cats):
        """Add record prompted by user into self._records"""        

        # Convert the string into a Record instance.
        input_list = input_str.split()
        if len(input_list) == 3:                                                    # check validity of input         
            try:
                category = input_list[0]                                            
                if cats.is_category_valid(category, cats.get_categories):    
                    description = input_list[1]
                    amount = int(input_list[2])                     
                    self._records.append(Record(category, description, amount))     # append Record into self._records
                else:
                    sys.stderr.write(error_message["CategoryNotFound_ADD"])
            except ValueError:                                  # dealing with invalid format of amount
                sys.stderr.write(error_message["InvalidAmountFormat"]) 
        else:                                                   # dealing with invalid format of input
            sys.stderr.write(error_message["InvalidFormat_ADD"])

    def view(self):
        """Show current records and report the balance."""

        print("Here's your expense and income records:\nCategory              Description           Amount\n--------------------  --------------------  ------")
        # enumerate to show index of records 
        for idx, record in enumerate(self._records):
                print(f"{idx + 1:<2d}: {record.get_category:<18s} {record.get_description:<21s} {record.get_amount}")
        print("--------------------------------------------------")
        balance = self._initial_money + sum([record.get_amount for record in self._records])
        print(f"Now you have {balance} dollars.\n")        

    def delete(self):
        """Delete specified record from current records"""

        # show current records for sack of user
        if len(self._records) == 0:
            sys.stderr.write("No record available to be removed\n")
        else:
            print("Current records:\nCategory              Description           Amount\n--------------------  --------------------  ------")
            for idx, record in enumerate(self._records):
                    print(f"{idx + 1:<2d}: {record.get_category:<18s} {record.get_description:<21s} {record.get_amount}")
            print("--------------------------------------------------")
            try:
                # prompt for index of item to delete
                idxDel = int(input("Which record do you want to delete?(eg: 2 #to delete item with index 2) "))
                if idxDel - 1 < 0:                                  # dealing with out of index problem
                    raise IndexError
                else:
                    del(self._records[idxDel - 1])                  # delete selected record
            except ValueError:                                      # dealing with invalid format of input
                sys.stderr.write(error_message["InvalidFormat_OTHERS"])
            except IndexError:                                      
                sys.stderr.write(error_message["OutOfIndex"])

    def find(self, target_cat):
        """Show the records under specified categoryand report the total amount of money of the listed records."""
        
        if target_cat == []:                                    # dealing with CategoryNotFound error
            sys.stderr.write(error_message["CategoryNotFound_FIND"])
            return
        filtered_records = list(filter(lambda x:x.get_category in target_cat, self._records))

        print(f"Here's your expense and income records under category \"{target_cat[0]}\":\nCategory              Description           Amount\n--------------------  --------------------  ------")

        for idx, record in enumerate(filtered_records):
            print(f"{idx + 1:<2d}: {record.get_category:<18s} {record.get_description:<21s} {record.get_amount}")
        print("--------------------------------------------------")
        target_cat_amount = sum([record.get_amount for record in filtered_records])
        print(f"The total amount above is {target_cat_amount}\n")
        
    def save(self):
        """Write the initial money and all the records to 'records.txt'."""

        with open("records.txt", 'w') as fh:
            # write initial_amount as first line
            fh.write(f"initial_amount {self._initial_money}\n")
            # create str list of records and write expensesList for the rest of lines
            recordsList = [" ".join([record.get_category, record.get_description, str(record.get_amount)]) + '\n' for record in self._records]
            fh.writelines(recordsList)

    def __repr__(self):
        return f'Records: {self._records}'

class Categories:
    """Maintain the category list and provide some methods."""

    def __init__(self):
        """Constructor of class 'Categories'"""        
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
    def view(self, cats, level = 0):
        """Show current categories with indended form"""

        if type(cats) is list:
            for cat in cats:
                self.view(cat, level + 1)
        else:
            print(f'{"  "* (level - 1) + "- "}{cats}')

    def is_category_valid(self, target_cat, cats):
        """Check whether specified category is included in categories"""
        
        if type(cats) is list:
            if target_cat in cats:
                return True
            else:
                for cat in cats:
                    if self.is_category_valid(target_cat, cat):
                        return True
                return False
        return False

    def find_subcategories(self, target_cat):
        """Return flattened list of specified category and its subcategories"""

        def find_subcategories_gen(target_cat, categories, found = False):
            if categories is None:
                return
            if type(categories) is list:
                for idx, cat in enumerate(categories):
                    yield from find_subcategories_gen(target_cat, cat, found)
                    if cat == target_cat:
                        try:
                            subcat = categories[idx + 1]
                            if type(subcat) is list:
                                yield from find_subcategories_gen(target_cat, subcat, True)
                        except IndexError:
                            pass
            else:
                if categories == target_cat or found == True:
                    yield categories
                    
        retcat = [cat for cat in find_subcategories_gen(target_cat, self._categories)]
        return retcat
    @property
    def get_categories(self):
        """getter method for categories list"""
        return self._categories

    def __repr__(self):
        return f'Categories: {self._categories}'

# start main program
categories = Categories()
records = Records()

while True:
    # prompt user for input of command
    command = input("\nWhat do you want to do (add / view / view categories / find / delete / exit)? ")
    
    if command == "add":                #dealing "add" command
        record = input("Add an expense or income record with categories, description, and amount (separate by spaces):\n(eg: meal breakfast -50) ")
        records.add(record, categories)
        
    elif command == "view":             #dealing "view" command
        records.view()

    elif command == "view categories":  #dealing "view categories" command
        categories.view(categories.get_categories)

    elif command == "find":             #dealing "find" command
        category = input("Which category do you want to find? ")
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)

    elif command == "delete":           #dealing "delete" command
        records.delete()

    elif command == "exit":             #dealing "exit" command
        records.save()
        break

    else:                               #dealing invalid command
        sys.stderr.write(error_message["InvalidCommand"])


