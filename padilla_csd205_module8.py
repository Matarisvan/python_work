# Luis Padilla
# 09/17/22
# CSD205 Module 8 Assignment


print("\nWelcome to the Miles to Kilometers Converter!\n")

try:
    miles = float(input("How many miles have you driven this past year? "))
    kilo = float(miles * 1.609)
except:
    print("error")
print("Every mile that you drive is 1.609 Kilometers!")

def drive():
    miles = float(input("miles"))
    if miles >=1:
        print("You have driven", kilo, "kilometers this year!")
    else:
        print("That is an impossible amount. Please Try again!\t")
        drive()
drive()



'''
if miles >= 1:
    pass
else:
    drive()
'''