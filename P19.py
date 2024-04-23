# Exercise 1: Modeling a Bank Account
class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Balance: {self.balance}")

acct1 = BankAccount("1234", "John Doe", 500)
acct2 = BankAccount("2345", "Jane Doe")

acct1.deposit(100)
acct1.check_balance() # Balance: 600

acct2.withdraw(200) # Insufficient funds