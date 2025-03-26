import random

# Get the user's choice
human_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

# ASCII Art for Rock, Paper, Scissors
rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""

paper = """
       _______
---'    ____)____
             ______)
           _______)
           _______)
 ---.__________)
"""

scissors = """
    _______
---'   ____)____
            ______)
           __________)
          (____)
---.__(___)
"""

# Variable to control the loop
continue_play = True

while continue_play:
    # Check the user's choice
    if human_choose == 0:
        print(rock)
        computer_choose = random.randint(0, 2)  # Generate a random choice for the computer
        if computer_choose == 1:
            print("Computer chose:\n" + paper + "\nYou lose")
        elif computer_choose == 2:
            print("Computer chose:\n" + scissors + "\nYou won")
        elif human_choose == computer_choose:
            print("Computer chose:\n" + rock + "\nDraw")
    elif human_choose == 1:
        print(paper)
        computer_choose = random.randint(0, 2)
        if computer_choose == 2:
            print("Computer chose:\n" + scissors + "\nYou lose")
        elif computer_choose == 0:
            print("Computer chose:\n" + rock + "\nYou won")
        elif human_choose == computer_choose:
            print("Computer chose:\n" + paper + "\nDraw")
    elif human_choose == 2:
        print(scissors)
        computer_choose = random.randint(0, 2)
        if computer_choose == 1:
            print("Computer chose:\n" + paper + "\nYou lose")
        elif computer_choose == 0:
            print("Computer chose:\n" + rock + "\nYou won")
        elif human_choose == computer_choose:
            print("Computer chose:\n" + scissors + "\nDraw")
    else:
        # Handle invalid input
        print("The input is not suitable. Please try again!")
        human_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

    # Ask the user if they want to play again
    if continue_play:
        one_More_Time = input("Do you want to play one more time? Type Y for \"Yes\" or N for \"No\"\n")
        if one_More_Time.upper() == "Y":
            continue_play = True
            human_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))  # Ask for input again
        elif one_More_Time.upper() == "N":
            continue_play = False  # Exit the loop
