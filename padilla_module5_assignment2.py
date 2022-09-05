# Luis Padilla
# 08/31/22
# CSD205 Module 5 Assignment
'''
feet under 100 =    $0.87
feet 100-249 =      $0.80
feet 250-499 =      $0.70
feet over 500 =     $0.50
'''

print("Welcome!")
name = input("What is your company name? ")
print("Welcome", name.title() + "!")
# The purpose for the paragraph above is to greet the user and to obtain the name of the user's company

print("The cost of optic fiber cable per foot starts at $0.87 with discounts for Bulk Purchases!\n$0.80 after 100 feet\n$0.70 after 250 feet\n$0.50 after 500 feet")
print
cost = (float(input("How many feet would you like? ")))
# The purpose here is to let the user know how much each foot costs and to obtain the amount of feet the user requires for their project
# The feet required is then multiplied by the cost to get a final amount of money

if cost <= 99:
    cost = cost * .87
elif cost <= 249:
    cost = cost * .80
elif cost <= 499:
    cost = cost * .70
else:
    cost = cost * .50
# This block of code is what determines by how much to multiply the number inputted by user

print(name.title() + ",", "Your total cost will be", "$" + str(cost))
# The purpose here is to finalize the user's experience with the program and inform them of a final cost
