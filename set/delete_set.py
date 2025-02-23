#  Write a Python Program to Remove all the items of set.


numbers = {1, 5, 3, 2, 32}

print("\nCurrent Set Elements: ")
print(numbers)

choice = input("\nAre you want delete all set elements(y/n): ")

if choice == "y":
    print("\nUpdated Set:")
    print({})
    numbers.clear()
