# Luis Padilla
# 09/19/22
# CSD205 Module 7 Assignment

'''
For this module, we will work with classes by creating a banking program. Your program will use the
inheritance diagram from this week in order to create a parent class and two child classes.
Your program will create an object of each type (CheckingAccount and SavingsAccount).

Your program will use the following data:
Balance: $200, $25
Fees: $5
Minimum Balance: $50
Interest Rate: 2%

You will need to run the program twice. Once with the account balance of $200 and once with the account
balance of $25. Since the second run of the program will have a balance lower than the minimum balance,
a message should be output letting the user know that their account is below the minimum balance.
Incorporate the good coding practices you have learned up to this point in the course such as
Try/Except Blocks, allow the user to continue to run the program, and to exit the program,
formatting methods, etc.
'''

# Defining Parent Class
class BankAct:
    def __init__(self,actNum, actBal):
        self.actNum = actNum
        self.actBal = float(actBal)
    def getActNum(self):
        return self.actNum
    def getBal(self):
        return self.actBal
    
    def deposit(self, dep):
        self.dep = dep
        depAmt = input("How much would you like to deposit?\t$")
        try:
            float(depAmt)
            self.actBal = float(self.actBal) + float(depAmt)
            print("Your balance is now $", self.actBal)
        except ValueError:
            print("Please enter an amount:")
            depAmt = input()

    def withdraw(self, wdrw):
        self.wdrw = wdrw
        self.actBal = self.actBal - wdrw

# Defining Child Class 1
class CheckingAct(BankAct):
    def __init__(self, actNum, actBal, fees, minBal):
        super().__init__(actNum, actBal)
        self.fees = fees
        self.minBal = minBal
    def getFees(self):
        return self.fees
    def getMinBal(self):
        return self.minBal

# Defining Child Class 2
class SavingsAct(BankAct):
    def __init__(self, actNum, actBal, intRate):
        super().__init__(actNum, actBal)
        self.intRate = intRate
        
    def addInt(self):
        return self.intRate

# 2 Different Accounts for each type of Child
milan1 = CheckingAct(1899, 200, 5, 50)
milan2 = SavingsAct(1899, 200, .02)
chelsea1 = CheckingAct(1905, 25, 5, 50)
chelsea2 = SavingsAct(1905, 25, .02)

print("\nWelcome to your local Bank!\n\nWhich account will you be using?")

# Selecting User
def selUser():
    global user
    user = input("Checking Account or Savings Account?\t")
    if user.lower() == "checking":
        user = milan1
    elif user.lower() == "savings":
        user = chelsea2
    else:
        selUser()
selUser()

# List of Options
options = (
"opt1 = check balance",
"opt2 = withdraw",
"opt3 = deposit",
"opt4 = check savings bal",
"opt5 = calc sav int")

# List of Valued Options
opt1 = "check balance",
opt2 = "withdraw",
opt3 = "deposit",
opt4 = "check savings bal",
opt5 = "calc sav int"
       
#
#
#
#
#

def main():
    print("\nPlease select an option between 1 and 5:\t")
    for opts in options:
        print(opts)
    option = input() 
    while True:
        try:
            float(option.range[1:6])
        except ValueError:
            print("\nError, please select an option:")
            for opts in options:
                print(opts)
            option = input()
        if options <= 5 and options >= 1:
            break
    while True:

        if option == "1":
            print(opt1)
            break
        elif option == "2":
            print(opt2)
            break
        elif option == "3":
            print(opt3)
            break
        elif option == "4":
            print(opt4)
            break
        elif option == "5":
            print(opt5)
            break
        
main()