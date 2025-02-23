# Write a Python Program to Get 5 Items from User to Store in a Set, to Display in Lower and Upper Case both.

words = set()

user_inputs = input("\nEnter a sentence: ")


user_inputs = user_inputs.split(" ")

for item in user_inputs:
    words.add(item)


print("\nSet items in upper case___")
for item in words:
    print(item.upper())


print("\nSet items in lower case___")
for item in words:
    print(item.lower())
