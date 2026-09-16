# Method 1: Using Python's built-in math library (The quick way)
import math

num1 = int(input("Enter a number to find its factorial (Math Module): "))
result1 = math.factorial(num1)
print("The factorial of", num1, "is", result1)

print("-" * 20) # Just prints a dividing line

# Method 2: Using a 'for' loop (The logic-building way)
num2 = int(input("Enter a number to find its factorial (Loop Method): "))
factorial = 1

# This loop multiplies our 'factorial' variable by every number up to num2
for i in range(1, num2 + 1):
    factorial = factorial * i

print("The factorial of", num2, "is", factorial)