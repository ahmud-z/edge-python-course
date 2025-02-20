# Write a Python Program to get Name of User that starts with ‘a’, otherwise Error Message Should Display

name = input("Enter a name: ")
name = name.lower()

if name.startswith("a"):
    print("Valid Name that starts with character 'a'")
else:
    print("Invalid name. It Dosen't start with 'a'")
