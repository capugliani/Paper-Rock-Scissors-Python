import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_password = []
for random_choice in range (0, nr_letters):
    choosen_letter = random.randint(0, len_letters - 1)
    letter = letters[choosen_letter]
    letter_password.append(letter)

symbol_password = []
for random_choice in range (0, nr_symbols):
    choosen_symbol = random.randint(0, len_symbols - 1)
    symbol = symbols[choosen_symbol]
    symbol_password.append(symbol)

number_password = []
for random_choice in range (0, nr_numbers):
    choosen_number = random.randint(0, len_numbers - 1)
    number = numbers[choosen_number]
    number_password.append(number)

joint_list = [*letter_password,*symbol_password,*number_password]

random.shuffle(joint_list)

print("Easy Level!")
print(''.join(letter_password+symbol_password+number_password))
print("\nHard Level!")
print(''.join(joint_list))