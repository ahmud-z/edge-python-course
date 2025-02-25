# Write a Python program that attempts to read a file named missing.txt. Use exception handling to catch the FileNotFoundError and print a message saying that the file does not exist.

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except:
    print("File not found")
