# Write a Python Program to get Name of User that starts with ‘a’, otherwise Error Message Should Display
# Write a Python Program to get Name of User that Ends with ‘n’, otherwise Error Message Should Display
# Write a Python Program to get a Sentence from User, And Display Character of that Sentence that Present on Odd Index Number


name = input("Enter a name: ")
name = name.lower()

if name.startswith("a"):
    print("Valid Name that starts with character 'a'")
else:
    print("Invalid name. It Dosen't start with 'a'")
