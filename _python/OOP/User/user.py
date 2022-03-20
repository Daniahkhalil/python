class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance +=amount

    def make_withdrawal(self,amount):
        self.account_balance -=amount
    
    def display_user_balance(self):
        print(self.name,self.account_balance)

user1=User("Dania","Dhkhalil99@gmail.com")
user2=User("Samia","samia@gmail.com")
user3=User("Qusay","Qusay@gmail.com")

user1.make_deposit(200)
user1.make_deposit(200)
user1.make_deposit(200)
user1.make_withdrawal(50)
user1.display_user_balance()
user2.make_deposit(200)
user2.make_deposit(200)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_balance()
user3.make_deposit(500)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_user_balance()


