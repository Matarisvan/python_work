# Luis Padilla
# 09/09/22
# CSD205 Module 7 Assignment

print("Hello! and Welcome to the Investment Calculator!\n\nWe are here to determine how long it takes to double your investment!")
money = float(input("How much money are you investing?\t$"))
rate = float(input("What is the interest rate?\t\t%")) * .01
total = 0
years = 1

while total <= (money * 2):
    change = money * rate
    total = total + change
    
    print(years, "$", total, change)
    years += 1
print("It took ", years - 1, " years to double your investment at an annually fixed percentage of ", rate,"%")
print("congratulations!")