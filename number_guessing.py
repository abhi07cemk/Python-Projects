import random

print("Welcome to the Number Guessing Game")

number_to_guess = random.randint(1,100)

while True:
    try:
        user_input = input("Please enter a number between 1 and 100: ")
        guess = int(user_input)

        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print("Congratulations! You guessed the number!")

    except ValueError:
        print("Enter A Valid Number")


