# program to calculate basic operations and for percentage to use it as discount.

# def the operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! cannot be divide by 0" if y == 0 else x / y
def percentage(x, y): return (x / 100) * y

# print the intro
print("---Welcome to the 1Calculater---")

while True:

    num1 = float(input("\nEnter the first number:"))
    op = input("Enter Operations: +,-,*,/,% ")
    num2 = float(input("Enter the second number:"))

    if op == "+": print(f"Result: {add(num1, num2)}")
    elif op == "-": print(f"Result: {subtract(num1, num2)}")
    elif op == "*": print(f"Result: {multiply(num1, num2)}")
    elif op == "/": print(f"Result: {divide(num1, num2)}")
    elif op == "%": print(f"Result: {percentage(num1, num2)} (which is {num1}% of {num2})")
    else: print("Invalid/Wrong operator")

    again = input("\nCalculate again? (y/n): ").lower()
    if again != 'y':
      print("Goodbye!")
      break
