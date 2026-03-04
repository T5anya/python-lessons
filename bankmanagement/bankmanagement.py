
import datetime
import random
import json
from pathlib import Path
import hashlib


class bank:
    def hashpin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    def loaddata(self):
        with open("data.json", "r") as file:
           return json.load(file)
    
    def savedata(self, data):
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def accountnumber(self):
        data=self.loaddata()
        accountno=str(random.randint(1000000000, 9999999999))
        if accountno not in data:
            return accountno
    
    #create account
    def createaccount(self):
        data=self.loaddata()
        name=input("enter your name: ")
        age=int(input("enter your age: "))
        if age<18:
            print("you are not eligible to create an account")
            return
        accountno=self.accountnumber()
        mobile=int(input("enter your mobile number: "))
        if len(str(mobile))!=10 and not str(mobile).isdigit():
            print("invalid mobile number")
            return
        email=input("enter your email: ")
        if "@" not in email or "." not in email :
            print("invalid email")
            return
        pin=str(input("enter your pin: "))# save the pin in hashed form for security
        if len(pin)!=4 and not str(pin).isdigit():
            print("invalid pin")
            return
        balance=0
        transactionhistory=[]
        data[accountno]={"name": name, "age": age, "mobile": mobile, "email": email, "pin":self.hashpin(pin),"balance": 0, "transactionhistory":[]}
        self.savedata(data)
        print("account created successfully")
        print("your account number is: ", accountno)
        print("please remember your account number and pin for future use")
        print("ur details are: ", data[accountno]["name"], data[accountno]["age"], data[accountno]["mobile"], data[accountno]["email"], data[accountno]["balance"],data[accountno]["transactionhistory"])

    #deposit money
    def deposit(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        if accountno not in data:
            print("account number not found")
            return
        pin=str(input("enter your pin: "))
        if self.hashpin(pin)!=data[accountno]["pin"]:
            print("invalid pin")
            return
        amount=int(input("enter the amount to be deposited: "))
        if amount<=0 or amount>100000:
            print("invalid amount")
            return
        data[accountno]["balance"]+=amount
        self.savedata(data)
        print("amount deposited successfully")
        print("your current balance is: ", data[accountno]["balance"])
        data[accountno]["transactionhistory"].append(
            f"Deposited ₹{amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        self.savedata(data)


    #withdraw money
    def withdraw(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        if accountno not in data:
            print("account number not found")
            return
        pin=str(input("enter your pin: "))
        if self.hashpin(pin)!=data[accountno]["pin"]: 
            print("invalid pin")
            return
        amount=int(input("enter the amount to be withdrawn: "))
        if amount<=0 or amount>100000:
            print("invalid amount")
            return
        if amount>data[accountno]["balance"]:
            print("insufficient balance")
            return
        data[accountno]["balance"]-=amount
        self.savedata(data)
        print("amount withdrawn successfully")
        print("your current balance is: ", data[accountno]["balance"])  
        data[accountno]["transactionhistory"].append(
            f"Withdrew ₹{amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        self.savedata(data)

    #check details of the account
    def checkdetails(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        pin=str(input("enter your pin: "))
        if accountno not in data or self.hashpin(pin)!=data[accountno]["pin"]:
            print("account number not found")
            return
        print("your details are: ", data[accountno]["name"], data[accountno]["age"], data[accountno]["mobile"], data[accountno]["email"], data[accountno]["balance"],data[accountno]["transactionhistory"])

    #show transcation history
    def transactionhistory(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        pin=str(input("enter your pin: "))
        if accountno not in data or self.hashpin(pin)!=data[accountno]["pin"]:
            print("account number not found")
            return
        print("your transaction history is: ", data[accountno]["transactionhistory"])
        
    #update details of the account
    def updatedetails(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        pin=str(input("enter your pin: "))
        if accountno not in data or self.hashpin(pin)!=data[accountno]["pin"]:
            print("account number not found")
            return
        print("what do you want to update?")
        print("enter 1 for updating name")
        print("enter 2 for updating age")
        print("enter 3 for updating mobile number")
        print("enter 4 for updating email")
        print("enter 5 for updating pin")
        choice=int(input("enter your choice: "))
        if choice==1:
            name=input("enter your name: ")
            data[accountno]["name"]=name
        elif choice==2:
            age=int(input("enter your age: "))
            if age<18:
                print("you are not eligible to create an account")
                return
            data[accountno]["age"]=age
        elif choice==3:
            mobile=int(input("enter your mobile number: "))
            if len(str(mobile))!=10 and not str(mobile).isdigit():
                print("invalid mobile number")
                return
            data[accountno]["mobile"]=mobile
        elif choice==4:
            email=input("enter your email: ")
            if "@" not in email or "." not in email :
                print("invalid email")
                return
            data[accountno]["email"]=email
        elif choice==5:
            pin=str(input("enter your pin: "))
            if len(str(pin))!=4 and not str(pin).isdigit():
                print("invalid pin")
                return
            data[accountno]["pin"]=self.hashpin(pin)
        else:
            print("invalid choice")
            return
        self.savedata(data)
        print("details updated successfully")

    #delete account
    def deleteaccount(self):
        data=self.loaddata()
        accountno=str(input("enter your account number: "))
        pin=str(input("enter your pin: "))
        if accountno not in data or self.hashpin(pin)!=data[accountno]["pin"]:
            print("account number not found")
            return
        del data[accountno]
        self.savedata(data)
        print("account deleted successfully")
       
b=bank()
while True:
    
    print("Welcome to the Bank Management System")
    print("enter 1 for creating an account")
    print("enter 2 for depoiting money")
    print("enter 3 for withdrawing money")
    print("enter 4 for checking details of the account")
    print("enter 5 for updating details of the account")
    print("enter 6 for showing transaction history")
    print("enter 7 for deleting the account")

    choic=int(input("enter your choice: "))
    if choic==1:
        b.createaccount()
    elif choic==2:
        b.deposit()
    elif choic==3:
        b.withdraw()
    elif choic==4:
        b.checkdetails()
    elif choic==5:
        b.updatedetails()
    elif choic==6:
        b.transactionhistory()
    elif choic==7:
        b.deleteaccount()
    else:
        print("invalid choice")