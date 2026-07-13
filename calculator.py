# CLI calculator project.
import json

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return x / y


def calculate(x, y, operation):
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return division(x, y)
    return None


def get_x_input():
    x_text = input("Enter (x) integer or (quit) to exit: ").strip().lower()
    if x_text == "quit":
        return "quit"

    if x_text == "history":
        return "history"
    
    try:
        x = int(x_text)

    except ValueError:
        print("Please enter a valid integer!")
        return None
    
    return x



def get_y_input():
    try:
        y_text = input("Enter (y) integer or (quit) to exit: ").strip().lower()

        if y_text == "quit":
            return "quit"
        
        y = int(y_text)

    except ValueError:
        print("Please enter a valid integer!")
        return None
    
    return y



def get_operation():
    operation = input("Enter an operation, (+, -, *, /): ").strip()
    return operation


def display_result(x, operation, y, result):
    print(f"{x} {operation} {y} = {result}")


def save_history(history, filename="history.json"):
    with open(filename, "w") as file:
        json.dump(history, file)


def load_history(filename="history.json"):
    try:
        with open(filename, "r") as file:
            history = json.load(file)

        return history
    
    except FileNotFoundError:
        return []


def main():
    history = load_history()

    while True:

        x = get_x_input()

        if x == "quit":
            break

        if x is None:
            continue

        if x == "history":
            if len(history) == 0:
                print("No history yet.")
                continue
            else:
                for item in history:
                    print(item)
            continue


        operation = get_operation()

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation!")
            continue

        y = get_y_input()

        if y == "quit":
            break

        if y is None:
            continue


        if operation == "/" and y == 0:
            print("Cannot divide by zero!")
            continue 


        result = calculate(x, y, operation)


        display_result(x, operation, y, result)

        calculation_text = f"{x} {operation} {y} = {result}"
        history.append(calculation_text)

        save_history(history)
        print("History saved")
        print("-" * 50)


if __name__ == "__main__":
    main()
    
