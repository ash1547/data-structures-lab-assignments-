  print("Balance:", self.balance)


# Creating object
b1 = BankAcc("123456789", 1000)

# Calling methods
b1.display_account()
b1.deposit(500)
b1.withdraw(200)
b1.check_balance()
