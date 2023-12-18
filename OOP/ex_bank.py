class Bank:
    def __init__(self,balance = 0):
        self.balance = balance

    def check_balance(self):
         print(f"your balance is : {self.balance}")
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit succesfull. Your balance is : {self.balance}")
        else:
            print("ivalid deposit amount please enter a valid amound ")
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdraw succesful. your balance is : {self.balance}")
        elif amount <= 0:
            print(f"invalid amound, enter valid amount")
        else:
            print("withdraw failed")
bank = Bank()

print(bank.check_balance())

print(bank.deposit(1000))

print(bank.withdraw(1500))

        
