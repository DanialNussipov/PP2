class Account():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print (f"you've added {money} $")
        print (f'Balance: {self.balance} $')
        
    def withdraw(self, money):
        self.balance -= money
        if self.balance < 0:
            print (f"You've tried to take {money}, but you dont have enough cash.")
            self.balance += money
            print (f'Balance: {self.balance} $')
        else:
            print (f"you've took {money} $")
            print (f'Balance: {self.balance} $')
    
meme = Account("Danial", 1000)
meme.deposit(5000)
meme.withdraw(2000)
meme.withdraw(2000)
meme.withdraw(2500)





        