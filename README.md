This repo consists of two python programs.

About Task 1.py:

It asks the user to enter a number, checks if it's even or odd, and handles errors if the input is not a valid number.

Step-by-step:
try:
→ This starts a block where we try to run some code that might cause an error.

a = int(input("Enter a number to be checked: "))
→ It asks the user to enter a number.
→ It tries to convert the input into an integer using int().

if a % 2 == 0:
→ It checks if the number divides evenly by 2 (i.e., no remainder).
→ If yes, it's an even number.

print(a, "is an even number.")
→ This line prints that the number is even.

else:
→ If the number does not divide evenly by 2…

print(a, "is an odd number")
→ It prints that the number is odd.

except ValueError:
→ If the user types something that isn't a valid whole number (like letters or special characters), this block runs.

print("Invalid input! Please enter a valid integer.")
→ It tells the user the input was wrong and asks for a proper number.

print("Thanks for checking!")
→ This line prints no matter what — it always says thank you at the end.



About Task 2.py:

This code adds all the numbers from 1 to 50 together and prints the result.

Step-by-step:
total_sum = 0
→ We start with a total of 0.

for i in range(1, 51):
→ We go through every number starting from 1 up to 50 (because range(1, 51) means 1 to 50, not including 51).

total_sum += i
→ Each number is added to the total.

print(...)
→ Finally, we print the total sum.

Thanks!
