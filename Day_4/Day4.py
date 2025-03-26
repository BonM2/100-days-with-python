# Day 4 I was learnt about how to create random number, list in python
import random as rd

# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.
random_integer = rd.randint(1, 1000)
print(random_integer)

# random.random() -> Returns the next random floating point number between [0.0 to 1.0)
random_float = rd.random()
print(random_float * 5)

love_score = rd.randint(1, 100)
print(f"Your love score is {love_score}")

# Virtual coin toss program
coin_flip = rd.randint(0, 1)
if coin_flip == 0:
    print("Tails")
else:
    print("Heads")

states_of_vietnam = ["Thành phố Hồ Chí Minh", "Bình Dương", "Vũng Tàu"]
states_of_vietnam.extend(["An Giang", "Tây Ninh"])
print(states_of_vietnam)

# Random name program
names_string = "Bảo, Như, Bum"
name = names_string.split(",")
random_index = rd.randint(0, len(name) - 1)
print(f"{name[random_index]} is going to buy meal today!")

# Find the treasure
line1 = [".", ".", "."]
line2 = [".", ".", "."]
line3 = [".", ".", "."]
Map = [line1, line2, line3]

print("Hiding your treasure! 'X' marks the spot.")
position = input("Enter a position (e.g., B2): ")  # Where do you want to place the treasure?

alphabet = ["A", "B", "C"]

# Extract the letter and number from the input
column_letter = position[0].upper()  # Convert to uppercase if needed
row_number = int(position[1])  # Convert row to an integer

# Find the position on the map
for j in range(len(alphabet)):  # Iterate through the alphabet to find the column
    if alphabet[j] == column_letter:
        Map[row_number - 1][j] = "X"  # Mark the position with 'X'
        break

# Print the map
print(f"{line1}\n{line2}\n{line3}")
