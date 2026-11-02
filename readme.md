# 🔐 Password Generator

A command-line password generator written in Python. You choose the password length and which character types to include, and the program builds a random password from them.

This is my first Python project, built step by step to learn the language coming from a Java background.

## ⚙️ How It Works

```
┌──────────────────────────┐
│ 1. Ask for length (8-64) │ ◄── re-asks on invalid input ("abc", "12.5", 3, 100)
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│ 2. Ask y/n for:          │
│    • uppercase letters   │ ◄── accepts y / yes / n / no, any case, extra spaces
│    • symbols             │
│    • numbers             │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│ 3. Build character pool  │     lowercase letters (always)
│                          │   + every group the user chose
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│ 4. Pick random characters│ ──► Your password: 4^LZI)ocQt^3&7#R
│    until length reached  │
└──────────────────────────┘
```

## 🛠️ Tech Stack

### Language & Standard Library
| Tool | Purpose |
|------|---------|
| **Python 3.10** | Programming language |
| **`string` module** | Ready-made character sets (`ascii_lowercase`, `ascii_uppercase`, `digits`, `punctuation`) |
| **`random` module** | Random selection of characters (`random.choice`) |

No external libraries are needed, only the Python standard library.

### Development Tools
| Tool | Purpose |
|------|---------|
| **PyCharm** | IDE |
| **venv** | Isolated virtual environment for the project |
| **Git** | Version control |
| **GitHub** | Remote repository |

## 🚀 How to Run

**Requirements:** Python 3.10 or newer.

1. Clone the repository:
   ```bash
   git clone https://github.com/Liakops7/password-generator.git
   cd password-generator
   ```
2. Run the program:
   ```bash
   # Windows
   python password_generator.py

   # Linux / macOS
   python3 password_generator.py
   ```

## 💻 Example

```
Password length (8-64): abc
Please enter a whole number.
Password length (8-64): 16
Include uppercase? (y/n): y
Include symbols? (y/n): maybe
Please answer with 'y' or 'n'.
Include symbols? (y/n): yes
Include numbers? (y/n): Y
Your password: 4^LZI)ocQt^3&7#R
```

## 📁 Project Structure

```
password-generator/
├── password_generator.py   # The whole program
├── .gitignore              # Keeps .idea/, .venv/ and __pycache__/ out of the repo
└── README.md
```

## 📚 Development Log

### Step 1 – Setup and the `string` module
Set up the project in PyCharm with a virtual environment and published it to GitHub with a `.gitignore`. Explored the `string` module and combined its character sets into one pool of 94 characters.

### Step 2 – First random password
Used `random.choice()` inside a `for _ in range(length)` loop to build a password one character at a time. Learned that Python uses indentation instead of `{ }` to define code blocks.

### Step 3 – User input and validation
Read the length with `input()` and converted it with `int()`. Used `try / except ValueError` to catch non-numeric input and a `while True` loop with `continue` / `break` to keep asking until the value is a whole number between 8 and 64. Caught only `ValueError` instead of a bare `except:` so that unexpected errors are not hidden.

### Step 4 – Choosing character types
Stored the questions and their character groups in two parallel lists and looped over them with `range(len(...))`, so a new character type can be added without repeating code. Cleaned answers with `.strip().lower()` and checked them against a tuple with `in`.

Bugs found and fixed along the way:
- The list held the *names* `"ascii_uppercase"` as text instead of the variables `string.ascii_uppercase`, so the letters of the word itself ended up in the pool.
- `answer in "y"` checks for a substring, and `"" in "y"` is `True`, so pressing Enter counted as "yes".
- `("y")` is just a string in parentheses. It is the comma that makes a tuple: `("y", "yes")`.

## 🗺️ Roadmap

- [x] Custom length with input validation
- [x] Choose uppercase letters, symbols and numbers


## 👤 Author

**Ilias Liakopoulos**, Computer Science graduate, Athens University of Economics and Business

GitHub: [@Liakops7](https://github.com/Liakops7)