# Write a Python Program to get Name of User that Ends with ‘n’, otherwise Error Message Should Display

name = input("Enter a name: ")
name = name.lower()

if name.endswith("a"):
    print("Valid Name that starts with character 'a'")
else:
    print("Invalid name. It Dosen't start with 'a'")
