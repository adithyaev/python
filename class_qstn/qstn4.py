class Account:
    def __init__(self,ac_no,ac_name,balance):
        self.ac_no = ac_no
        self.ac_name = ac_name
        self.balance = balance
    
    def define_acount(self):
        
        print(f"account number: {self.ac_no}")
        print(f"account name : {self.ac_name}")
        print(f"balance: {self.balance}")



acnt1 = Account(1,'adithya',2000)
print(acnt1.ac_no)
print(acnt1.ac_name)
print(acnt1.balance)
print(acnt1.define_acount())

        