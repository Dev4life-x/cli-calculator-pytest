# CLI Calculator + Pytest

A command-line calculator built with Python, automated tests, JSON history, and input validation.

## Features

* Add, subtract, multiply, and divide integers
* Validate numeric input
* Reject unsupported operation symbols
* Prevent division by zero
* Exit from the first or second number prompt
* Save calculations to a JSON history file
* Display saved calculations with the `history` command
* Verify calculator and history functions with Pytest

## Project Structure

```text
cli-calculator-pytest/
├── calculator.py
├── tests/
│   └── test_calculator.py
├── README.md
├── requirements.txt
└── .gitignore
```

`history.json` is created automatically when calculations are saved. It is ignored by Git because it contains local runtime data.

## Requirements

* Python 3.10 or newer
* Pytest

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd cli-calculator-pytest
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project requirements:

```bash
python -m pip install -r requirements.txt
```

## Run the Calculator

```bash
python calculator.py
```

Follow the prompts to enter:

1. The first integer
2. An operation
3. The second integer

## Example

```text
Enter (x) integer or (quit) to exit: 10
Enter an operation, (+, -, *, /): +
Enter (y) integer or (quit) to exit: 5
10 + 5 = 15
History saved
--------------------------------------------------
```

## Commands

At the first-number prompt:

```text
history
```

Displays previous calculations.

```text
quit
```

Exits the program.

The `quit` command also works at the second-number prompt.

## Run the Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run only calculation-selector tests:

```bash
python -m pytest -v -k "calculate"
```

Run only history tests:

```bash
python -m pytest -v -k "history"
```

The test suite covers:

* Normal arithmetic operations
* Zero and negative numbers
* Division by zero
* Operation selection
* Invalid operations
* Saving JSON history
* Loading JSON history

## What I Learned

* How to split a program into focused functions
* How to separate calculation logic from CLI flow
* How to validate input with `try` and `except`
* How to handle invalid operations and division by zero
* How to save and load JSON data
* How to write automated tests with Pytest
* How to use temporary files safely in tests
* How to use Git commits as development checkpoints
* How to publish and tag a finished project on GitHub

## Release

Current stable release:

```text
v1.0.0
```

The project is feature-frozen. Future changes should be limited to important bug fixes.
