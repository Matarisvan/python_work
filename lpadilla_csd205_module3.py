# Luis Padilla
# 08/20/22
# CSD205 Module 3 Assignment

print("Welcome!")
name = input("What is your company name? ")
print("Welcome", name.title() + "!")
# The purpose for the paragraph above is to greet the user and to obtain the name of the user's company

print("The cost of optic fiber cable per foot is $0.87")
cost = (float(input("How many feet would you like? "))) * .87
# The purpose here is to let the user know how much each foot costs and to obtain the amount of feet the user requires for their project
# The feet required is then multiplied by the cost to get a final amount of money

print(name.title() + ",", "Your total cost will be", "$" + str(cost))
# The purpose here is to finalize the user's experience with the program and inform them of a final cost