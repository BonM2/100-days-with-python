import random as rd

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_pw = int(input("How many letters would you like in your password?\n"))
symbol_pw = int(input("How many symbols would you like?\n"))
number_pw = int(input("How many numbers would you like?\n"))

password_list = []

# Thêm ký tự chữ
password_list.extend(rd.choice(letters, k=letter_pw))
# Thêm ký tự đặc biệt
password_list.extend(rd.choices(symbols, k=symbol_pw))
# Thêm số
password_list.extend(rd.choices(numbers, k=number_pw))

# Xáo trộn danh sách mật khẩu để ngẫu nhiên hơn
rd.shuffle(password_list)

# Chuyển danh sách thành chuỗi
final_password = "".join(password_list)

print(f"Here is your password: {final_password}")