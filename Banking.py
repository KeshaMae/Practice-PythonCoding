from msilib.schema import SelfReg
from typing_extensions import Self


class User():
    def __init__(self,name,age,gender) :
       self.name = name
       self.age = age
       self.gender = gender

    def showDetails(self) :
      print("Personal Details")
      print("")
      print("Name ", self.name)
      print("Age ", self.age)
      print("Gender ", self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super() .__init__(name,age,gender)
        self.balance = 0
    
    def deposit(amount):
        SelfReg.amount = amount
        Self.balance = Self.balance + Self.amount
        print("Account balance is updated : ₱", Self.balance)

    def widthraw(self,amount) :
        SelfReg.amount = amount
        if SelfReg.amount > Self.balance:
            print("Insufficient Funds | Balance Available : ₱",self.balance)
        else:
            self.balance = self.balance - SelfReg.amount
            print("Account balance is updated : ₱", self.balance)
        

