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



class BankAct:
    def __init__(self,actNum, actBal):
        self.actNum = actNum
        self.actBal = actBal
    def getActNum(self):
        return self.actNum
    def getBal(self):
        return self.actBal
    
    def deposit(self, dep):
        self.dep = dep
        self.actBal = self.actBal + dep 

    def withdraw(self, wdrw):
        self.wdrw = wdrw
        self.actBal = self.actBal - wdrw

class CheckingAct(BankAct):
    def __init__(self, actNum, actBal, fees, minBal ):
        super().__init__(self, actNum, actBal)
        self.fees = fees
        self.minBal = minBal
    def getFees(self):
        return self.fees
    def getMinBal(self):
        return self.minBal

class SavingsAct(BankAct):
    def __init__(self, actNum, actBal, intRate):
        super().__init__(self, actNum, actBal)
        self.intRate = intRate
        
    def addInt(self):
        return self.intRate


Milan = BankAct("1899", "200")
Chelsea = BankAct("1905", "25")


def main():
    print("\nWelcome to your local Bank!\nWhich account will you be using?\n")
    user = input("Are you a Milan fan or a Chelsea fan?\t")
    userT = True
    while userT:
        try:
            if user.lower() == "milan":
                Milan()
            elif user.lower() == "chelsea":
                Chelsea()
        except:
            user = input()
        else:
            userT = False
main()
        
