class User:
    def __init__(self, name,email, BankAccount):
        self.name = name
        self.email = email
        self.bank = BankAccount	# added this line

    def make_deposit(self,amount):
        self.bank.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.bank.withdrawal(amount)
        return self
    
    def display_user_balance(self):
        print(self.name,self.email)
        return self

class BankAccount:
    def __init__(self,int_rate,balance):
        self.balance=balance
        self.int_rate=int_rate
        

    def deposit(self,amount):
        self.balance +=amount
        return self

    def withdrawal(self,amount):
        if self.amount > self.balance :
            print("amount greater than balance")
        else:
            self.balance -=amount
            return self
    
account1=BankAccount(0.02,200)
dania=User("dania","Daniahkhalil99@gmail.com",account1)
dania.make_deposit(200)
dania.display_user_balance()

 