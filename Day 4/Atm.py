# create a class called Atm which has 3 instances- pin,balance=0,menu->choice 1-to create pin, 2- to deposit amt,
# 3- to withdraw, 4- to check the balance, 5- to exit the machine. 1-input pin and print created succesfully.
# 2- compare pin. if correct, input deposit amount & update balance, else, print invalid pin.
# 3- validate pin, withdraw amt< balance, else print insufficient fund
# 4- validate pin, print balance
class atm:

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def create_pin(self):
        self.pin = int(input("Create a new 4 digit pin"))
        p = int(input("Confirm pin"))
        if p == self.pin:
            print("New pin created")
        else:
            print("Incorrect pin")
            print("Try again")

    def deposit(self):
        x = int(input("Enter pin"))
        if (x == self.pin):
            damt = float(input("Enter deposit amount"))
            print(f"{damt} amount deposited")
            self.balance = self.balance + damt
            print(f"New balance = {self.balance}")
        else:
            print("Invalid pin")

    def withdraw(self):
        x = int(input("Enter pin"))
        if (x == self.pin):
            wamt = float(input("Enter withdraw amount"))
            if (wamt < self.balance):
                print(f"{wamt} amount deposited")
                self.balance = self.balance - wamt
                print(f"New balance = {self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    def check(self):
        x = int(input("Enter pin"))
        if (x == self.pin):
            print(f"Balance= {self.balance}")
        else:
            print("Invalid pin")


p = int(input("Welcome new user! Enter a 4 digit pin to activate your account"))
c = atm(p, 0)
a = 1
while a != 0:
    print("Choose from the menu options given below")
    choice = int(input("1- to create new pin. 2- to deposit amount. 3- to withdraw amount. 4- to check balance. 5- exit"))
    if choice == 1:
        c.create_pin()
    elif choice == 2:
        c.deposit()
    elif choice == 3:
        c.withdraw()
    elif choice == 4:
        c.check()
    elif choice == 5:
        break
    else:
        print("Invalid input")
print("Thank you for choosing Canara bank")
