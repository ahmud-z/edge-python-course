# Write a Python Program to get 5 Words from the user. Iterate that List to Display only those Word that starts with “b”.

user_input = input("Enter some words separated space: ")
words = user_input.split(" ")


for word in words:
    if word.startswith("b"):
        print(word)
