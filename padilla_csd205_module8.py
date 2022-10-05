# Luis Padilla
# 09/17/22
# CSD205 Module 8 Assignment


print("\nWelcome to the Miles to Kilometers Converter!\n")

miles = (input("How many miles have you driven this past year?\n"))
kilo = float(1.609)
crtNum = True

# loop to check if value entered is a number(float in this situation)
while crtNum:
    try:
        float(miles)
    except ValueError:
        print("Error, please enter a number")
        miles = input()
    else:
        crtNum = False

miles = float(miles) # changing miles type to make sure it can be multiplied with kilo

dist = miles * kilo # formula that converts miles into kilometers

print(f"\nYou have driven ", miles, "miles! That is the same as ", dist, "kilometers!")
print("\nEvery mile that you drive is 1.609 Kilometers!\n")
