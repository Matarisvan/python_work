# Luis Padilla
# 08/20/22
# CSD205 Module 3 Assignment

print("Welcome!")
name = input("What is your company name? ")
print("Welcome", name.title() + "!")
print("The cost of optic fiber cable per foot is $0.87")
cost = (float(input("How many feet would you like? "))) * .87
print(name.title() + ",", "Your total cost will be", "$" + str(cost))