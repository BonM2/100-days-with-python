import random as rd

# Define character sets
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Add random letters
for i in range(0, num_letters):
    password_list.extend(rd.choice(letters))
# Add random symbols
for i in range(0, num_symbols):
    password_list.extend(rd.choice(symbols))
# Add random numbers
for i in range(0, num_numbers):
    password_list.extend(rd.choice(numbers))

# Shuffle the password list to make it more random
rd.shuffle(password_list)

# Convert the list to a string
final_password = ""
for i in range(0, len(password_list)):
    final_password += password_list[i]

print(f"Here is your password: {final_password}")
