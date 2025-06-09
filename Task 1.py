
try:
    a = int(input("Enter a number to be checked: "))
    if a % 2 == 0:
        print(a, "is an even number.")
    else:
        print(a, "is an odd number")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
print("Thanks for checking!")