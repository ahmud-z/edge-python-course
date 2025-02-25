# Write a Python Program to Create a SET in Such a way that user able to Remove any Item.

numbers = {12, 3, 4, 5, 6}


print("Current Set Items__")
print(numbers)


del_value = int(input("Which value you want to delete: "))

numbers.discard(del_value)

print("\nUpdated Set items: ")
print(numbers)
