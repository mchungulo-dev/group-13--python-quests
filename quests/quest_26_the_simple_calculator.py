# quest_26_the_simple_calculator.py

# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

# Get user input
print("--- The Alchemist's Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

# Use if-elif-else to call the correct function
if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation chosen.")