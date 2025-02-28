class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited  {amount} to your account") 
    
    def withdraw(self,amount):
        print(f"Withdraw  {amount} to your account")
        if(amount>self.balance):
            print("Not enough balance!!  ")
        else:
            self.balance-=amount
            print("Successfully withdraw........")
    def __str__(self):
        return f"Account Holder Name: {self.name}\nBalance: {self.balance}"
obj=BankAccount("Ritesh",1000)
print(obj)
obj.deposit(200)
obj.withdraw(500)
print(obj)


