import random


class Bank:
    def __init__(self, name: str, total_money: float, ):
        self.bank_name = name
        self.money = total_money
        self.accounts = []
    
    #def add_account(self, account_id: str, first_name: str, last_name: str, incomes: list, expenses: list):
    def add_account(self, account_id: str, person_total_income: float):
        self.money += person_total_income
        self.accounts.append(account_id)
    
    def delete_account(self, account_id: str, person_total_income: float):
        self.money -= person_total_income
        self.accounts.remove(account_id)
    
    def income(self, total_deposit: float):
        self.money += total_deposit

    def expense(self, total_withdraw: float):
        self.money -= total_withdraw

    def bank_info(self):
        print(f"BANK NAME: {self.bank_name}")
        print(f"TOTAL MONEY: {self.money}")
        print("ACCOUNTS IN BANK: ")
        for account in self.accounts:
            print("    " + account)
        print()

class PersonAccount:
    def __init__(self, bank_name: str, account_id: str, first_name: str, last_name: str, incomes = [0.00], expenses = [0.00]):
        self.bank_name = bank_name
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses
    
    def account_info(self):
        print(f"BANK NAME: {self.bank_name}")
        print(f"ACCOUNT ID: {self.account_id}")
        print(f"NAME: {self.first_name} {self.last_name}")
        print(f"TOTAL INCOME: {self.incomes[len(self.incomes)-1]}")
        print(f"TOTAL EXPENSES: {self.expenses[len(self.expenses)-1]}")
        print()
    
    def total_income(self):
        for i in range(len(self.incomes)):
            if i != len(self.incomes)-1:
                if self.incomes[i] > 0:
                    print(f"DEPOSIT: {self.incomes[i]}")
                else:
                    print(f"WITHDRAW: {self.incomes[i]}")
            else:
                print(f"TOTAL INCOME: {self.incomes[i]}")
        print()
    
    def total_expense(self):
        for i in range(len(self.expenses)):
            if i != len(self.expenses) - 1:
                print(f"EXPENSE {i+1}: {self.expenses[i]}")
            else:
                print(f"TOTAL EXPENSE: {self.expenses[i]}")
    
    def add_income(self, bank: Bank, income: float):
        if income <= 0:
            print(f"Invalid Income")
        self.incomes.insert(len(self.incomes) - 1, income)
        self.incomes[len(self.incomes)-1] += income
        Bank.income(bank, income)
        print(f"NEW TOTAL INCOME OF BANK ACCOUNT WITH ID {self.account_id}: {self.incomes[len(self.incomes)-1]}")
        print()
    
    def add_expense(self, bank: Bank, expense:float):
        if expense <= 0:
            print(f"Invalid Expense")
        self.expenses.insert(-2, expense)
        self.expenses[len(self.expenses)-1] += expense
        negative_income = expense*-1
        self.incomes.insert(len(self.incomes) - 1, negative_income)
        self.incomes[len(self.incomes)-1] += negative_income
        Bank.expense(bank, expense)
        print(f"NEW TOTAL EXPENSE OF BANK ACCOUNT WITH ID {self.account_id}: {self.expenses[len(self.expenses)-1]}")
        print(f"NEW TOTAL INCOME OF BANK ACCOUNT WITH ID {self.account_id}: {self.incomes[len(self.incomes)-1]}")
        print()


Metrobank = Bank("Metrobank", 100000.0121)
Michael = PersonAccount("Metrobank", "12132", "Michael", "Wheeler", [9100, -100, 9000], [100, 100])

Michael.account_info()
Metrobank.add_account("12132", Michael.incomes[len(Michael.incomes)-1])
Metrobank.bank_info()
Michael.add_income(Metrobank, 100)
Michael.add_expense(Metrobank, 100)
Michael.account_info()
Metrobank.bank_info()

Michael.total_income()
Michael.total_expense()