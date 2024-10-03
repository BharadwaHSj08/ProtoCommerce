class Customer:

    Bank_Name = "Axis bank"

    def __init__(self,name,Balance = 0.0):
        self.name = name
        self.Balance = Balance


    def Deposit(self,amount):
        self.Balance = self.Balance + amount
        print("Balance after Deposit :", self.Balance)

    def Withdrwal(self,amount):
        if amount > self.Balance:
            print("In sufficient Funds")

        else:
            self.Balance = self.Balance - amount
            print("Balance after Withdrawl :",self.Balance)

print("Welcome to :", Customer.Bank_Name)
name = input("Enter Name:")
c= Customer(name)

while True:

    print("Please Choose your Service\n D = Deposit, W = Withdrawl, E = Exit")
    option = input("Enter the Required Service:")
    if option.lower() == "d":
        amount = float(input("Enter the Amount:"))
        c.Deposit(amount)

    elif option.lower() == "w":
        amount = float(input("Enter the Amount:"))
        c.Withdrwal(amount)

    elif option.lower() == "e":
        print("Thanks for Banking")
        break

    else:
        print("Please choose one of our services to Utilise")
