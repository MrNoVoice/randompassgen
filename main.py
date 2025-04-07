import random
import string

def generate_password(min_length, special_characters=True, numbers=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    pwd = ""
    meets_criteria = False 
    has_special_character = False
    has_number = False

    while not meets_criteria or len(pwd) < min_length:
        new_character = random.choice(characters)
        pwd += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special_chars:
            has_special_character = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special_character

    return pwd

min_length = int(input("What is the minimum length of the password you want? "))
has_numbers = input("Do you want numbers in your password (y/n)? ").lower() == 'y'
has_special_characters = input("Do you want special characters in your password (y/n)? ").lower() == 'y'

pwd = generate_password(min_length, has_special_characters, has_numbers)
print(pwd)
