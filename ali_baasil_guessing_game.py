5# Baasil Ali
# 12 / 14 / 2022
#
# This program creates a guessing game which asks the user
# to try and guess the humber between 1 and 100. We define
# one function and use it to count the number of guesses.

import random

# Define the function play_guessing_game that accepts the number to guess as an argument
def play_guessing_game(number):
    # Initialize the number of guesses to 0
    guesses = 0

    # Repeatedly ask the user to guess a number from 1-100, or enter 0 to quit guessing
    while True:
        # Get the user's guess
        guess = int(input("Enter your guess 1-100, or enter 0 to stop guessing: "))

        # Check if the user entered 0
        if guess == 0:
            # If the user entered 0, display "You didn't guess my number" and tell them what the number was
            print("You didn't guess my number. It was", number)
            break

        # Check if the user's guess is higher than the random number
        if guess > number:
            # If the user's guess is higher than the random number, display "Too high, try again"
            print("Too high, try again.")

        # Check if the user's guess is lower than the random number
        if guess < number:
            # If the user's guess is lower than the random number, display "Too low, try again"
            print("Too low, try again.")

        # Check if the user's guess is equal to the random number
        if guess == number:
            # If the user's guess is equal to the random number, congratulate the user and tell them how many guesses they made
            print("Congratulations! You guessed my number in", guesses, "guesses.")
            break

        # Increment the number of guesses
        guesses += 1

# Repeatedly generate a random number in the range 1 through 100, and ask the user to guess what the number is
while True:
    # Generate a random number in the range 1 through 100
    number = random.randint(1, 100)

    # Call the function play_guessing_game and pass the number as an argument
    play_guessing_game(number)

    # Ask the player if they want to play again, accepting "Y" for yes or "N" for no in either upper or lower case
    again = input("Do you want to play again (y/n)? ")

    # Check if the user answered "N"
    if again.lower() == "n":
        # If the user answered "N", end the program
        print("Goodbye. Thanks for playing.")
        break
