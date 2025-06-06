This repo consists of two python programs.

About Task 1.py:

This small Python script prompts the user for two numbers, converts them into floats, calculates their sum, difference, product, and quotient (when possible), and then displays each result. Here’s a step-by-step description:

1. Prompt the user for two inputs.
2. Convert the inputs to floating-point numbers
3. Compute addition, subtraction, and multiplication

Add = a + b
Calculates the sum of a and b and stores it in a variable named Add.

Sub = a - b
Calculates a minus b and stores it in Sub.

Mul = a * b
Calculates a times b and stores it in Mul.
4. Print the results of those three operations
5. Attempt division and handle “divide by zero” errors

The code wraps the division in a try–except block:

Inside the try, Div = a / b calculates the quotient. If b is not zero, this line succeeds and prints “Division: ” along with the result (for example, if a = 5 and b = 2, it prints “Division: 2.5”).

If b is zero, Python would normally raise a ZeroDivisionError. In that case, execution jumps to the except block, which prints a friendly message:
Error: You can't divide by zero!
This prevents the program from crashing and informs the user that division by zero is not allowed.

About Task 2.py:

This script:
1. Takes the user's first and last name as input,
2. Combines them into a full name, and
3. Prints a personalized greeting using an f-string.

Line by line explanation:
--> Asks the user to type their first name.
--> The input is stored in a variable called a.
--> Asks for the last name, stored in variable b.
--> Combines the first name (a) and last name (b) with a space between them.
--> Stores the result in the variable fn (full name).

print(f"Hello, {fn}! Welcome to the Python program.")
Uses an f-string to insert the full name into a custom greeting.

Thanks!
