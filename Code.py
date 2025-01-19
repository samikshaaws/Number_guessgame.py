import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# Generating a random number between 1 and 100
secret_number = random.randint(1, 100)

# Number of attempts the player has
attempts = 0

# Loop until the player guesses the correct number
while True:
    # Get the player's guess
    guess = input("Enter your guess: ")

    # Check if the input is a valid number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    # Convert the guess to an integer
    guess = int(guess)
    
    # Increase the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break  # End the game
    