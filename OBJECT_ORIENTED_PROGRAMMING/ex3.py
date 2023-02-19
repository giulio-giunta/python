# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance=0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        return self.balance

    def withdraw(self, num):
        self.balance -= num
        return self.balance


acct = BankAccount("Darcy")

print(acct.owner)  # Darcy
print(acct.balance)  # 0.0
print(acct.deposit(10))  # 10.0
print(acct.withdraw(3))  # 7.0
print(acct.balance)  # 7.0
