class BankAccount:
    def __init__(self,account_balance=0):
        self.account_balance=account_balance
    def deposit(self,amount):
        self.account_balance += amount
        print(f"Deposited:${self.account_balance}")
    def withdraw(self,amount):
        self.account_balance=amount
        self.account_balance -=amount
        if self.account_balance >= 0:
            print(f"Current Balance: ${amount}")
            return True
        else:
            print(f"Insufficient funds.")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")