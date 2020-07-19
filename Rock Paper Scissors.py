import random

score = 0

def get_choice():
    global score

    choice = input("Make your choice from 'rock', 'paper', 'scissors' : ").lower()

    human_choice = {
        'rock': 0,
        'paper': 1,
        'scissors': 2,
    }[choice]

    comp_choice = random.randint(0, 2)

    computer_option = {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }[comp_choice]

    if comp_choice == human_choice:
        print("It's a tie")

    elif (comp_choice - human_choice) % 3 == 1:
        score -= 1
        print("Computer's choice is " + computer_option)
        print("Computer won")
        print("Your score: " + str(score))

    elif (comp_choice - human_choice) % 3 == 2:
        score += 1
        print("Computer's choice is " + computer_option)
        print("You won")
        print("Your score: " + str(score))


def rerun():
    for rerun in range(10000):
        get_choice()

rerun()