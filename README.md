# CLI Calculator

A beginner-friendly command-line calculator built with Python.

This project supports basic arithmetic operations, input validation, and calculation history saved in JSON.


## Features

* Add, subtract, multiply, and divide numbers
* Handle invalid number input
* Prevent division by zero
* Save calculation history in a JSON file
* Show calculation history with the `history` command
* Exit the program with the `quit` command


## How to Run

Run the program from the terminal:

```bash
python3 calculator.py
```

Then follow the prompts to enter two numbers and choose an operation.


## Example Usage

```text
Enter (x) integer or (quit) to exit: 10
Enter an integer, (y): 5
Enter an operation, (+, -, *, /): +
10 + 5 = 15
History saved


## Project Files

* `calculator.py` — main Python program
* `history.json` — saves calculation history
* `README.md` — explains the project
* `.gitignore` — ignores Python cache files


## What I Learned

- How to split a program into smaller functions
- How to validate user input with `try` and `except`
- How to handle division by zero
- How to save and load data with JSON
- How to use Git commits as project checkpoints
- How to write a basic README for a Python project