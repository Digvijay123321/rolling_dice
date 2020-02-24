import random

def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled
def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input('''Ready to roll?
            \tEnter=Roll. Q=Quit. :''')
        if roll_again.lower() == "q":
            rolling=False
        else:
            num_rolled = roll(sides)
            print("\t\tYou rolled : ",num_rolled)

    print("\t \t Thanks for playing!!")
main()
