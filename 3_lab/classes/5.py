class Account():
    def __init__(self, _owner, _balance):
        self.owner = _owner
        self.balance = _balance
    
    def show(self):
        print(f"owner: {self.owner}, balance: {self.balance}")

    def deposit(self, money):
        self.balance = self.balance + money        
        print(f"{money} dollar was added to your balance")

    def withdraw(self, x):
        if x <= self.balance:
            self.balance = self.balance - x 
        else:
            print(f"Your balance is lower than your request") 
        
var = Account("pp2", 100)
var.show()
var.deposit(500)
var.show()
var.withdraw(80)
var.show()