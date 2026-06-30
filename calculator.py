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
        y_text = input("Enter an integer, (y): ").strip()
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



def save_history(history):
    with open("history.json", "w") as file:
        json.dump(history, file)



def load_history():
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []
    
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

    
    y = get_y_input()

    if y is None:
        continue
 
    
    operation = get_operation()

    if operation == "+":
        result = add(x, y)
        
        

    elif operation == "-":
        result = subtract(x, y)
        
        

    elif operation == "*":
        result = multiply(x, y)
        

    elif operation == "/":
        if y == 0:
            print("Cannot divide by zero!")
            continue
        result = division(x, y)
        
   
    else:
        print("Invalid operation!")
        continue



    display_result(x, operation, y, result)
    
    calculation_text = f"{x} {operation} {y} = {result}"
    history.append(calculation_text)

    save_history(history)
    print("History saved")
    print("-" * 50)
