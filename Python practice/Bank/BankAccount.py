class BankAccount:
    def __init__(self,name,balance) -> None:
        self.name=name
        self.balance=balance
    def Deposit(self,amount):
        self.balance+=amount
        print(f"{self.balance}")
    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance-=amount
            print(f"{self.balance}")
        else:
            print("you dont have available balance")
    def __str__(self) -> str:
        return f"Account_holderName: {self.name}\nYour Balance: {self.balance}"

ba=BankAccount("annie",1000)
print(ba)
ba.Deposit(100)
ba.withdraw(500)
print(ba)


        
    