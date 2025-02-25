# Write a Python program that creates a file named data.txt and writes the
# following lines to it:
# Line 1: Welcome to Python programming.: Line 2: File handling is important for data management.:
# Line 3: Enjoy coding!

with open("data.txt", "w") as file:
    file.write(
        "Welcome to Python programming.\nFile handling is important for data management.\nEnjoy coding!"
    )

