import random

# Day 7 - Hangman Project
# A simple implementation of the classic Hangman word guessing game

print("Welcome to the Hangman game!")

# Game setup
words = ["sticker", "tutorial", "category"]  # List of possible words
random_word = random.choice(words)  # Randomly select a word
time_to_try = 6  # Number of allowed incorrect guesses
guess_word = ["_"] * len(random_word)  # Track correctly guessed letters

# Main game loop
while time_to_try > 0:
    # Display current game state
    print(" ".join(guess_word))
    print(f"You have {time_to_try} tries left.")

    # Get and validate user input
    c = input("Guess a letter: ").lower()
    while len(c) > 1 or not c.isalpha():  # Ensure input is a single letter
        print("Please enter a single letter.")
        c = input("Guess a letter: ").lower()

    # Check if letter is in the word
    found = False
    for i in range(len(random_word)):
        if c == random_word[i]:
            guess_word[i] = c  # Reveal the letter
            found = True

    # Handle incorrect guess
    if not found:
        time_to_try -= 1
        print(f"Wrong guess! You have {time_to_try} tries left.")

    # Check for win condition
    if "_" not in guess_word:  # All letters guessed
        print("Congratulations! You won!")
        print(f"The word was: {random_word}")
        break

    # Handle lose condition (only check after loop ends)
    if time_to_try == 0 and "_" in guess_word:
        print("Game over! You lost.")
        print(f"The word was: {random_word}")