# Luis Padilla
# 08/28/22
# CSD205 Module 4 Assignment

print("Hello Python! Welcome to Assignment #4!\n")
#this is a welcome code to engage the user

premteams = ("Chelsea", "Arsenal", "Man City", "Tottenham", "Brighton", "Leeds United", "Newcastle", "Man United", "Liverpool", "Brentford", "Fulham", "Crystal Palace", "Southampton", "Nottingham Forest", "Aston Villa", "West Ham", "Bournemouth", "Everton", "Wolves", "Leicester City")
premz = list(premteams)
premz.sort()
premteams = tuple(premz)
print(f"The names of the teams competeing in the English Premier Leagure are: {premteams}")
print(f"There are ", len(premteams), " teams competing in the Premier League!\n")
# I made a tuple of the 20 teams in the 2022/2023 Premier League,
# changed it into a list so I could sort it alphabetically,
# and then changed it back into a tuple before displaying it to the user
# I used the len() function to display how many values are within the tuple

for premteam in premteams:
    print(f"{premteam.title()} competes in the Premier League")
#This iterates through each of the 20 individual values and prints them out with a string of text

print(" ")
# this is to separate the printed tuples in the terminal

def teamsprem():
    premz.reverse()
    premteams = tuple(premz)
    for premteam in premteams:
        print(f"{premteam} has a chance at being this year's Champion!")
teamsprem()
# Here I made a function "teamsprem" to sort the tuple in reverse alphabetical order by using the list "premz" i had made above and again changing it back into a tuple
# then i made a for loop so i could iterate each value into a line of text by itself and on the next line i used print() to display it along with a string
# I made a function so the original tuple "premteams" does not get changed into reverse order permanently