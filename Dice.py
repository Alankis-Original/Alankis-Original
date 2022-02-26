import random
Minimum = int(input("Minimum: "))
Maximum = int(input("Maximum: "))
while True:
    Dice = random.randint(Minimum, Maximum)
    input("press enter to roll: ")
    print("You Got:", Dice)