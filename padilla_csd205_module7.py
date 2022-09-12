# Luis Padilla
# 09/09/22
# CSD205 Module 7 Assignment

print("\nHello! and Welcome to the Investment Calculator!\n\nFind out how many years it takes to double your investment at a fixed annual rate!")
money = float(input("How much money are you investing?\t$"))
rate = float(input("What is the interest rate?\t\t%"))
percent = rate * .01
total = 0
years = 1
perYear = money * percent

print()

while total <= (money * 2):    
    total = total + perYear
    #print(years, "$" + str(total)) # print this to see each year's total
    years += 1
print("It took ", years - 1, " years to double your investment at an annually fixed percentage of ", rate,"%")
print("Congratulations! Your investment brought in $" + str(perYear), " every year!\n")