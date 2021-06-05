class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance = 0): 
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        self.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if(self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance + self.balance*self.int_rate
        return self
    @classmethod
    def all_balances(cls):
        print(f"Accounts: {len(cls.accounts)}")
        for account in cls.accounts:
            print(f"Balance: {account.balance}\nInterest Rate: {account.int_rate}")

account1 = BankAccount(0.01)
account2 = BankAccount(0.02)
account1.deposit(100).deposit(200).deposit(400).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(200).withdraw(400).withdraw(100).yield_interest().display_account_info()
print(BankAccount.accounts[0].balance)
BankAccount.all_balances()