# while and looping
"""
looping = True
while looping == True:
    answer = input("Como te llamas?")
    if answer == "Angeles":
        looping = False
    else:
        print("Vete a la verga")
print("Hi Bookinhaha!")
"""
"""
target = input("metale un pinche numero: ")
target = int(target)
total = 0
sigue = 1
while sigue <= target:
    total = total + sigue
    print("added in", sigue, "total por ahora es", total)
    sigue = sigue + 1
print("la suma de los numeros del 1 al", target, "es:", total)
"""

"""
i = 0
while i <= 10:
    print(i)
    i = i + 1
"""
'''
total = 0.0
count = 0
x = float(input("meta un numero y uno negativo para cerrar sesion "))
while x >= 0:
    total = total = 1
    count = count + 1
    x = float(input("meta un numero y uno negativo para cerrar sesion "))
print("muchas gracias")
'''


#Classes Inheritance

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname + " " + self.lastname
class Employee(Person):
    def __init__(self, first, last, employeeNum):
        Person.__init__(self, first, last)
        self.employeeNum = employeeNum
    def GetEmployee(self):
        return self.Name() + ", " + self.employeeNum

exPerson = Person("Mark", "Zuckerberg")
exEmployee = Employee("Bill", "Gates", "1983")

print(exPerson.Name())
print(exEmployee.GetEmployee())

'''
#Overriding Classes
class SavingsAccount:
    def __init__(self):
        self.interestRate = 2
    def getRate(self):
        return self.interestRate
class MoneyMarket(SavingsAccount):
    def getRate(self):
        return self.interestRate + 1

savings = SavingsAccount()
market = MoneyMarket()

print(savings.getRate())
print(market.getRate())
'''