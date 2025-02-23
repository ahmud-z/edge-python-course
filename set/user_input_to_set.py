# Write a Python Program to Create a Set, then take any Item from User to Update that Set.


data = {1, 2, 3, "A", "B", "c"}

print("Set Items: ")
print(data)

userInput = input("Enter a name or a number: ")


print("\nUpdated Set: ")
if userInput.isnumeric():
    data.add(int(userInput))
else:
    data.add(userInput)

print(data)
