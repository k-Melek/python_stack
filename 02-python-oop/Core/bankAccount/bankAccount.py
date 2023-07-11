class BankAccount:
    accounts = []

    def __init__(self, interest_rate=0, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("you have insufficient funds.")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            print(f"Interest Rate: {account.interest_rate}, Balance: {account.balance}")

# Create two accounts
account1 = BankAccount(0.3, 1500)
account2 = BankAccount(2, 1500)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1.deposit(300).deposit(300).deposit(300).withdraw(500).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(100).deposit(100).withdraw(100).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()

#  use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_accounts_info()