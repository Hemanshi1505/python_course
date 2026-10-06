# OOPS (inheritence, abstraction, polymorphism)

# class student: # class
#     def __init__(self, name, age): # init fun - data
#         self.name = name # self - object
#         self.age = age

#     def display(self): # fun inside the class called method
#         print(self.name)
#         print(self.age)

# result = student("hemanshi", 21) # Creating an object
# result.display()


# Task - bank ##########################
class bank():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def balance(self,amount):
        self.bal = amount

    def deposit(self, amount):
        self.bal += amount

    def withdrawl(self, amount):
        if amount <= self.bal:
            self.bal -= amount
        else:
            print("Insufficient Balance")
        

name = str(input("Enter Account Holder name = "))
age = int(input("Enter Account Holder age = "))
account = bank(name, age)
print("your bank Account is created")

amount = int(input("Enter deposit amount = "))
account.balance(amount)
print("Total balance = ",account.bal);

request = str(input("Do you have Any Request = "))
if request == "yes":
    req = int(input("press 1 for deposit and 2 for withdrawl!"))
    if req == 1:
        amount = int(input("Enter deposit amount = "))
        account.deposit(amount)
        print("Total balance = ",account.bal)
    elif req == 2:
        amount = int(input("Enter withdrawl amount = "))
        account.withdrawl(amount)
        print("Total balance = ",account.bal)
    else:
        print("Invalid option")
else:
    print("okay! thanks")


