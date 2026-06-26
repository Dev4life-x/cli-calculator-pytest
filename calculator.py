# CLI calculator project.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return x / y

while True:

    x_text = input("Enter (x) integer or q to quit: ")

    if x_text == "q":
        break
    try:
        x = int(x_text)
    except ValueError:
        print("Please enter a valid integer!")
        continue

    try:
        y = int(input("Enter an integer, (y): "))
    except ValueError:
        print("Please enter a valid integer!")
        continue

    operation = input("Enter an operation, (+, -, *, /): ")


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

    print(f"{x} {operation} {y} = {result}")
    print("-" * 40)

