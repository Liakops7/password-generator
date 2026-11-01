# Import the built-in "string" module.
# A module is a file of ready-made code that we can reuse.
# "string" comes with Python, so we don't need to install anything.
import string

# Module for generating random values
import random

all_characters = (
    string.ascii_lowercase
)

MIN_LENGTH = 8
MAX_LENGTH = 64
# Keep asking until the user gives a valid number.
# "while True" loops forever; we leave it with "break" once the input is OK.
while True:
    user_input = input(f"Password length ({MIN_LENGTH}-{MAX_LENGTH}): ")

    try:
        # Try converting the text to an integer
        length = int(user_input)
    except ValueError:
        # int() failed, e.g. the user typed "abc" or "12.5"
        print("Please enter a whole number.")
        continue  # Skip the rest of this iteration and ask again

    # If we got here, it's a number; now check that it's in range.
    # Python allows chained comparisons: a <= x <= b
    if MIN_LENGTH <= length <= MAX_LENGTH:
        break  # Valid input, exit the loop
    else:
        print(f"The length must be between {MIN_LENGTH} and {MAX_LENGTH}.")

questions = ["uppercase", "symbols", "numbers"]
character_groups = [string.ascii_uppercase, string.punctuation, string.digits]

for i in range(len(questions)):
    while True:
        # Clean the answer: remove surrounding spaces and make it lowercase
        answer = input(f"Include {questions[i]}? (y/n): ").strip().lower()

        # A real tuple: the COMMA between the values is what makes it a tuple.
        # "in" now checks if answer is EQUAL to one of the values,
        # not if it appears INSIDE a string.
        if answer in ("y", "yes"):
            all_characters += character_groups[i]
            break
        elif answer in ("n", "no"):
            break
        else:
            print("Please answer with 'y' or 'n'.")

# Start with an empty string; we'll add characters to it one by one
password = ""
# range(length) produces the numbers 0, 1, 2, ..., 11 (12 numbers in total).
# The loop body therefore runs exactly 12 times.
# We name the loop variable "_" because we don't actually use its value;
# this is a common Python convention meaning "I don't care about this variable".
for _ in range(length):
    # Pick one random character from the pool and append it to the password
    password += random.choice(all_characters)

print("Your password:", password)
