class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into the account.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from the account.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # Dictionary to store user's accounts

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Account '{account_name}' does not exist for user '{self.name}'.")

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Account '{account_name}' does not exist for user '{self.name}'.")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            balance = self.accounts[account_name].get_balance()
            print(f"User '{self.name}' account '{account_name}' balance: {balance}")
        else:
            print(f"Account '{account_name}' does not exist for user '{self.name}'.")

    def transfer_money(self, amount, other_user, from_account_name, to_account_name):
        if from_account_name in self.accounts and to_account_name in other_user.accounts:
            if self.accounts[from_account_name].get_balance() >= amount:
                self.accounts[from_account_name].withdraw(amount)
                other_user.accounts[to_account_name].deposit(amount)
                print(f"Transferred {amount} from user '{self.name}' account '{from_account_name}' "
                        f"to user '{other_user.name}' account '{to_account_name}'.")
            else:
                print(f"Insufficient balance in user '{self.name}' account '{from_account_name}'.")
        else:
            print(f"Either user '{self.name}' or user '{other_user.name}' does not have the specified account(s).")


# Example usage
user1 = User("Alice")
user2 = User("Bob")

# Create and display user1's accounts
user1.accounts["Savings"] = BankAccount()
user1.accounts["Checking"] = BankAccount()
print(f"{user1.name}'s accounts:", user1.accounts.keys())

# Deposit to user1's Savings account
user1.make_deposit("Savings", 1000)
user1.display_user_balance("Savings")  # Output: User 'Alice' account 'Savings' balance: 1000

# Withdraw from user1's Checking account
user1.make_withdrawal("Checking", 500)
user1.display_user_balance("Checking")  # Output: User 'Alice' account 'Checking' balance: -500

# Transfer money from user1 to user2
user1.transfer_money(200, user2, "Savings", "Checking")
user2.display_user_balance("Checking")  # Output: User 'Bob' account 'Checking' balance: 200