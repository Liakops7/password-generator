# Import the built-in "string" module.
# A module is a file of ready-made code that we can reuse.
# "string" comes with Python, so we don't need to install anything.
import string

# string.ascii_lowercase holds all lowercase English letters (a-z)
print("Lowercase:", string.ascii_lowercase)

# string.ascii_uppercase holds all uppercase English letters (A-Z)
print("Uppercase:", string.ascii_uppercase)

# string.digits holds the digits 0-9
print("Digits:", string.digits)

# string.punctuation holds the special symbols, e.g. ! @ # $ %
print("Symbols:", string.punctuation)

# We can join strings with "+" to build one big "pool" of characters.
# Later, the password will be built by picking characters from this pool.
all_characters = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + string.punctuation
)

print("All characters:", all_characters)

# len() returns how many characters a string has
print("Total characters available:", len(all_characters))