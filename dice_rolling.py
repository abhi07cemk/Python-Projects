import random

rolls = 0

while True:
    choice = input("Roll the dice? (y/n): ").strip().lower()

    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        rolls += 1
        print("Dice:", die1, die2)
        print("Total:", die1 + die2)

    elif choice == "n":
        print("Total rolls:", rolls)
        print("Thanks for playing!")
        break

    else:
        print("Please enter y or n")
