#Assignment_1 from python course
#Task1 - Perform Basic Mathematical Operations.


a=input('Enter the first number:  ')
b=input('Enter the second number:  ')
a=float(a)
b=float(b)
Add=a+b
Sub=a-b
Mul=a*b
print("Addition: ",Add)
print("Subtraction: ", Sub)
print("Multiplication: ", Mul)
try:
    Div=a/b
    print("Division: ", Div)
except ZeroDivisionError:
    print("Error: You can't divide by zero!")


