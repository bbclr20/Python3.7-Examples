import bank

# __init__
acct = bank.Account("ben", "12345", 1000)

# mathods
acct.deposit(5000)
acct.withdraw(200)

# __str__
print(acct)
print(str(acct))

# gettter
print(f"{acct.name}, {acct.id}, {acct.balance}")

# setter
acct.name = "Ben"
acct.id = "1234567"
acct.balance = 2000
print(acct)

# static method
bank.Account.info()

# class method
print(bank.Account.default())
