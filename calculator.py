# CLI calculator project.

def add(x, y):
    return x + y



def subtract(x, y):
    return x - y



def multiply(x, y):
    return x * y



def division(x, y):
    return x / y



def get_x_input():
    x_text = input("Enter (x) integer or (quit) to exit: ")
    if x_text == "quit":
        return "quit"
    
    try:
        x = int(x_text)
    except ValueError:
        print("Please enter a valid integer!")
        return None
    
    return x



def get_y_input():
    try:
        y = int(input("Enter an integer, (y): "))
    except ValueError:
        print("Please enter a valid integer!")
        return None
    
    return y



def get_operation():
    operation = input("Enter an operation, (+, -, *, /): ")
    return operation



def display_result(x, operation, y, result):
    print(f"{x} {operation} {y} = {result}")


history = []

while True:
    
    x = get_x_input()

    if x == "quit":
        break

    if x is None:
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
    print()
    calculation_text = f"{x} {operation} {y} = {result}"
    history.append(calculation_text)
    print(f"history = {history}")
    

    print("-" * 50)
