# Write a Python Program to Create a set of different numbers, and user should be able to add new item to set.

numbers = {1, 2, 3, 4, 5, 6}

print("\nCurrent set elements: ")

print(numbers)

choice = input("\nAre you want to add any element(y/n): ")

if choice == "y":
    item = int(input("Enter a number to add: "))
    numbers.add(item)
    print("\nUpdated set items: ")
    print(numbers)
