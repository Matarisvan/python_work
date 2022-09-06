# Luis Padilla
# 09/05/22
# CSD205 Module 6 Assignment: Dictionaries

print("\nWelcome! Shown below are a sample of players for AC Milan, the current champions of Italy!\n") # Welcome Message

milan = {
    "2" : "Davide Calabria",
    "4" : "Ismael Bennacer",
    "8" : "Sandro Tonali",
    "9" : "Olivier Giroud",
    "10" : "Brahim Diaz",
    "11" : "Zlatan Ibrahimovic",
    "12" : "Fikayo Tomori",
    "16" : "Mike Maignan",
    "17" : "Rafael Leao",
    "19" : "Theo Hernandez",
    "20" : "Pierre Kalulu",
    "23" : "Fikayo Tomori",
    "30" : "Junior Messias",
    "56" : "Alexis Saelemaekers",
    "90" : "Charles De Ketelaere"
} # Dictionary

for number, player in milan.items(): # gives a value to both the key and value in milan dictionary
    print(number, player)
print()
# number = milan.keys()
# player = milan.values()

fav = (input("Selct your favorite number from this list! ")) # asks user to select a number from dictionary
play = milan.get(fav) # takes number inputted by user (fav) and uses it to access dictionary
print()

if fav in milan:    # checks to see if input is a key within dictionary
    print("You have selected " + fav + " which is " + play) # if it is, it proceeds to display number selected along with its value
else:
    print("Sorry, but the number you chose is not a player on the list!")   # if not, display error message