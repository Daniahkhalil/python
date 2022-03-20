class BankAccount:
    def __init__(self,name,email,balance,int_rate):
        self.name=name
        self.email=email
        self.balance=0
        self.int_rate=int_rate
        

    def deposit(self,amount):
        self.balance +=amount
        return self

    def withdrawal(self,amount):
        self.balance -=amount
        return self
    
    def display_user_info(self):
        print(self.name,self.email,self.balance)
        return self

    def yield_interest(self):
        if(self.balance  > 0):
            self.balance+=self.balance*self.int_rate
        return self

user1=BankAccount("Dania","Dhkhalil99@gmail.com",200,2)
user2=BankAccount("Samia","samia@gmail.com",500,2)


user1.deposit(200).deposit(200).deposit(200).withdrawal(50).yield_interest().display_user_info() 
user2.deposit(200).deposit(200).withdrawal(100).withdrawal(50).withdrawal(50).withdrawal(50).withdrawal(50).yield_interest().display_user_info()
	
  