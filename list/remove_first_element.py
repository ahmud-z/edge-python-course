# Write a Python Program to get 5 items from user to store in a list. User should be able to remove first item of the list.

nums = input("Enter some numbers(separated by space): ")
str_numbers = nums.split(" ")

numbers = []

for i in str_numbers:
    numbers.append(int(i))

print("\nGiven List of Numbers: ", end="")
print(numbers)


choice = input("\nAre you want to remove item? (y/n): ")

if choice == "y":
    numbers.remove(numbers[0])
    print("\nList with removed first item:")
    print(numbers)
else:
    print("\nList without remove first item:")
    print(numbers)
