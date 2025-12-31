import random

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
choices = ('r', 'p', 's')

def get_winner(user, computer):
    if user == computer:
        return "Tie!"
    if (user == 'r' and computer == 's') or \
       (user == 's' and computer == 'p') or \
       (user == 'p' and computer == 'r'):
        return "You win!"
    return "You lose!"

while True:
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", emojis[user_choice])
    print("Computer chose:", emojis[computer_choice])
    print(get_winner(user_choice, computer_choice))

    if input("Play again? (y/n): ").lower() == 'n':
        print("Exiting...")
        break
