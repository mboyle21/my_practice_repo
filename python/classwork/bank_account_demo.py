from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)
account1.deposit(1000)
print(account1)

account2 = BankAccount("5678", 10000000000)
print(account2)
account2.deposit(13)
print(account2)
account2.withdraw(5000)
print(account2)
account2.get_balance()
print(account2)