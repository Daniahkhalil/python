class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_balance=0
        

    def make_deposit(self,amount):
        self.account_balance +=amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    
    def display_user_balance(self):
        print(self.name,self.account_balance)
        return self

user1=User("Dania","Dhkhalil99@gmail.com")
user2=User("Samia","samia@gmail.com")
user3=User("Qusay","Qusay@gmail.com")

user1.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
user2.make_deposit(200).make_deposit(200).make_withdrawal(100).make_withdrawal(100).display_user_balance()
user3.make_deposit(500).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()


