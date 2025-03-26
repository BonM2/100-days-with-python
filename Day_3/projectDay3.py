print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
direct = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if direct.lower() == "right":
    print("Fall into a hole. Game over.")
else:
    next_direct = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if next_direct.lower() == "swim":
        print("Attacked by trout. Game over.")
    else:
        choose_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")

        if choose_color.lower() == "blue":
            print("Eaten by beasts. Game over.")
        elif choose_color.lower() == "red":
            print("Burned by fire. Game over.")
        elif choose_color.lower() == "yellow":
            print("You Win!")
        else:
            print("Game over.")

