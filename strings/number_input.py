# Write a Python Program to accept only Number as String from User not Alpha or Special Character.

while True:
    numeric_input = input("Enter your input: ")

    if numeric_input.isdigit():  # Call the method by adding parentheses
        print("Valid Input Type!")
        break
    else:
        print("Invalid input, please provide a numeric input")
