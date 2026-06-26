# CLI calculator project.

import sys
while True:

    x_text = input("Enter (x) integer or q to quit: ")

    if x_text == "q":
        break
    
    x = int(x_text)

    y = int(input("Enter an integer, (y): "))
    operation = input("Enter an operation, (+, -, *, /): ")

    if operation == "+":
        
        result = x + y
        print()

    elif operation == "-":
        
        result = x - y
        print()

    elif operation == "*":
        
        result = x * y
        print()
    
    elif operation == "/":
      
        result = x / y
        print()
    
    else:
        print("Invalid operation!")
        continue

    print(f"{x} {operation} {y} = {result}")
    print("_ _" * 40 )

