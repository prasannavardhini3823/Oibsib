import random

def generate_password():
    length = int(input("Enter password length: "))
    want_letters = input("Include letters? (yes/no): ")
    want_numbers = input("Include numbers? (yes/no): ")
    want_symbols = input("Include symbols? (yes/no): ")

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_+"

    all_chars = ""
    
    if want_letters.lower() == "yes":
        all_chars += letters
    if want_numbers.lower() == "yes":
        all_chars += numbers
    if want_symbols.lower() == "yes":
        all_chars += symbols

    password = ""
    for i in range(length):
        password += random.choice(all_chars)

    print("Your generated password is:", password)
#if you want to generate the password again without restarting the script.
while True:
    generate_password()
    repeat = input("Do you want to generate another password? (yes/no): ")
    if repeat.lower() != "yes":
        break