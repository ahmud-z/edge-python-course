# Write a Python Program to get a Sentence from User to Display Total Number of Character, and Convert into Uppercase if not.

name = input("Enter your name: ")
total_char = len(name)

print(f"Hello, {name}")
print(f"Your name contains total {total_char} characters")

if name != name.isupper():
    name = name.upper()

print(f"Your name in Uppercase: {name}")
