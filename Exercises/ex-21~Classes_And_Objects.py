import os
import math
os.system('cls' if os.name == 'nt' else 'clear')

# Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and range. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self, list):
        self.list = list
        self.sum = 0
        self.med = 0
        self.sorted_list = sorted(self.list)
        self.count = len(self.sorted_list)

    def mean(self):
        for number in self.list:
            self.sum += number
        avg = self.sum/len(self.list)
        print(f"Mean: {math.ceil(avg)}")    

    def median(self):
        mid = self.count // 2
        if self.count % 2 != 0:
            self.med = self.sorted_list[mid]
        else:
            self.med = (self.sorted_list[mid - 1] + self.sorted_list[mid]) / 2
        print(f"Median: {math.ceil(self.med)}")

    def mode(self):
        from collections import Counter
        freq = Counter(self.list)
        mode_list = freq.most_common(1)
        mode_tuple = mode_list[0]
        mode = mode_tuple[0]
        count = mode_tuple[1]

        print(f'Mode: {mode}, Count: {count}')

    def range(self):
        max_val = self.sorted_list[len(self.sorted_list)-1]
        min_val = self.sorted_list[0]
        range = max_val - min_val
        print(f"Range: {range}")
    
data = Statistics(ages)
data.mean()
data.median()
data.mode()
data.range()

# Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties 
# and it has add_income, add_expense and account_balance methods. 

class PersonAccount:
    def __init__(self, firstname, lastname, income, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expenses = expenses

    balance = 0

    def add_income(self):
        self.balance += self.income
        print("Income added")
        self.account_balance()


    def add_expense(self):
        self.balance -= self.expenses
        print("Expenses taken into account")
        self.account_balance()

    def account_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

def main():
    person  =  PersonAccount('John','Dalton',250,180)
    person.account_balance()
    person.add_income()
    person.add_expense()

main()