import random
import string

print("🔐 Password Generator")

# Ask for password length
length = int(input("Enter password length: "))

# Ask which character types to include
use_letters = input("Include letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Create character set
characters = ""

if use_letters:
    characters += string.ascii_letters

if use_numbers:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

# Check if at least one type is selected
if characters == "":
    print("Please select at least one character type.")
else:
    password = ""

    # Generate password using loop
    for i in range(length):
        password += random.choice(characters)

    print("Your generated password is:", password)