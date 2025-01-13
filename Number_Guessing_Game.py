#Number guessing game

import random
def number_guess_game():
    number =random.randint(1,100)
    guess_taken =0
    print("welcome to Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100. ")

    while True:
        guess = int(input("Enter your guess:"))
        guess_taken +=1

        if guess<number:
            print("Too low!")
        elif guess>number:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {guess_taken} attempts.")
            break

number_guess_game()
