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

target = input("metale un pinche numero: ")
target = int(target)
total = 0
sigue = 1
while sigue <= target:
    total = total + sigue
    print("added in", sigue, "total por ahora es", total)
    sigue = sigue + 1
print("la suma de los numeros del 1 al", target, "es:", total)