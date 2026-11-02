import string
import random

all_characters = (
    string.ascii_lowercase
)

MIN_LENGTH = 8
MAX_LENGTH = 64

# Ask until a valid length is given
while True:
    user_input = input(f"Password length ({MIN_LENGTH}-{MAX_LENGTH}): ")

    try:
        length = int(user_input)
    except ValueError:
        print("Please enter a whole number.")
        continue

    if MIN_LENGTH <= length <= MAX_LENGTH:
        break
    else:
        print(f"The length must be between {MIN_LENGTH} and {MAX_LENGTH}.")

questions = ["uppercase", "symbols", "numbers"]
character_groups = [string.ascii_uppercase, string.punctuation, string.digits]

# Add each selected character group to the pool
for i in range(len(questions)):
    while True:
        answer = input(f"Include {questions[i]}? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            all_characters += character_groups[i]
            break
        elif answer in ("n", "no"):
            break
        else:
            print("Please answer with 'y' or 'n'.")

# Build the password from random characters
password = ""
for _ in range(length):
    password += random.choice(all_characters)

print("Your password:", password)
