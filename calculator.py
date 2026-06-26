# CLI calculator project.

def add(x, y):
    return x + y



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
        result = x - y
        

    elif operation == "*":
        result = x * y

    elif operation == "/":
        if y == 0:
            print("Cannot divide by zero!")
            continue
        result = x / y    
   
    else:
        print("Invalid operation!")
        continue

    print(f"{x} {operation} {y} = {result}")
    print("-" * 40)

