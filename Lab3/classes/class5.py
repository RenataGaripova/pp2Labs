class Account:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, money): #making new deposit
        self.balance += money

    def withdraw(self, money): #withdraw money from balance
        if (self.balance >= money):
            self.balance -= money
        else:
            print("Not enough money on your balance")



Acc1 = Account(5000, "Tom")

Acc1.withdraw(2500)

print(Acc1.balance)

Acc1.withdraw(2500)

print(Acc1.balance)

Acc1.withdraw(300)

print(Acc1.balance)

Acc1.deposit(1000)

print(Acc1.balance)

Acc1.withdraw(30)

print(Acc1.balance)
