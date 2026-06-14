import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.load(fs)
        else:print("no such file exists")
    except Exception as err:
        print(f"an exception occured:{err}")

    @classmethod
    def __update(cls):
        print("Database path:", Path(cls.database).absolute())
        print("before saving data:", Bank.data)
        with open(cls.database,'w') as fs:
            json.dump(Bank.data, fs, indent=4)
        print("data saved successfully")

    @classmethod
    def __generate_account_number(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=2)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)
    
    def createaccount(self):
        info={
            "name":input("enter your name:"),
            "age":input("enter your age:"),
            "email":input("enter your email:"),
            "pin":int(input("enter your pin:")),
            "accountnumber":Bank.__generate_account_number(),
            "balance":0
        }
        if (int(info["age"]))<18 or len(str(info["pin"]))!=4:
            print("sorry you cannot create an account")
        else:
            print("account created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please note down your account number")
            Bank.data.append(info)
            print("Current Bank.data =", Bank.data)

            Bank.__update()

    def depositmoney(self):
        accnumber=input("please tell your account number ")
        pin=int(input("please tell your pin aswell ")) 
        # print("Bank Data:", Bank.data)

        userdata=[i for i in Bank.data if i['accountnumber'] == accnumber and i['pin'] == pin]
        
        if  not userdata:
            print("sorry data not found")
            print("userdata =", userdata)
        else:
            amount=int(input("how much you want to deposit"))
            if amount >10000 or amount<=0:
                print("sorry the amount should be less than 10000 and greater than 0")

            else:
                userdata[0]['balance'] +=amount
                Bank.__update()
                print("money deposited successfully")
    
    def withdrawmoney(self):
        accnumber=input("please tell your account number ")
        pin=int(input("please tell your pin aswell ")) 
        # print("Bank Data:", Bank.data)

        userdata=[i for i in Bank.data if i['accountnumber'] == accnumber and i['pin'] == pin]
        
        if  not userdata:
            print("sorry data not found")
            print("userdata =", userdata)
        else:
            amount=int(input("how much you want to withdraw"))
            if userdata[0]['balance']<amount:
                print("sorry you have insufficient balance")

            else:
                userdata[0]['balance'] -=amount
                Bank.__update()
                print("money withdrawn successfully")
    
    def accountdetails(self):
        accnumber=input("please tell your account number ")
        pin=int(input("please tell your pin aswell ")) 
        # print("Bank Data:", Bank.data)

        userdata=[i for i in Bank.data if i['accountnumber'] == accnumber and i['pin'] == pin]
        
        if  not userdata:
            print("sorry data not found")
        else:
            print("account details:\n\n\n")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")
    
    def updateaccount(self):
        accnumber=input("please tell your account number ")
        pin=int(input("please tell your pin aswell ")) 
    
        userdata=[i for i in Bank.data if i['accountnumber'] == accnumber and i['pin'] == pin]
        if not userdata:
            print("sorry data not found")

        else:
            print("you can update your name, email and pin")

            print("fill the details you want to update or leave it blank if you don't want to update it")

            newdata={
                "name":input("enter your name or press enter to skip: "),
                "email":input("enter your email or press enter to skip: "),
                "pin":input("enter your pin or press enter to skip: ")
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]["name"]
            if newdata["email"]=="":
                newdata["email"]=userdata[0]["email"]
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]["pin"]
            
            newdata['age']=userdata[0]['age']
            newdata['accountnumber']=userdata[0]['accountnumber']
            newdata['balance']=userdata[0]['balance']

            if newdata['pin'] != "":
              newdata['pin'] = int(newdata['pin'])
            else:
              newdata['pin'] = userdata[0]['pin']
 
            for i in newdata:
                if newdata[i]== userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            Bank.__update()
            print("account updated successfully")
    
    def deleteaccount(self):
        accnumber=input("please tell your account number ")
        pin=int(input("please tell your pin aswell ")) 
    
        userdata=[i for i in Bank.data if i['accountnumber'] == accnumber and i['pin'] == pin]
        if not userdata:
            print("sorry data not found")

        else:
            check=input("are you sure you want to delete your account? (yes/no): ")
            if check == 'no' or check == 'No':
                print("account deletion cancelled")
            elif check == 'yes' or check == 'Yes':
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("account deleted successfully")

if __name__ == "__main__":

    user = Bank()

    print("press 1 for creating an account")
    print("press 2 for depositing the money in the bank")
    print("press 3 for withdrawing the money from the bank")
    print("press 4 for details of the account")
    print("press 5 for updating an account")
    print("press 6 for deleting an account")

    check = int(input("enter your choice: "))

    if check == 1:
        user.createaccount()

    elif check == 2:
        user.depositmoney()

    elif check == 3:
        user.withdrawmoney()

    elif check == 4:
        user.accountdetails()

    elif check == 5:
        user.updateaccount()

    elif check == 6:
        user.deleteaccount()
        