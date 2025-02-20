nums = input("Enter some numbers(separated by space): ")
str_numbers = nums.split(" ")

numbers = []

for i in str_numbers:
    numbers.append(int(i))

print("\nGiven List of Numbers: ", end="")
print(numbers)


choice = input("\nAre you want to remove item? (y/n): ")

if choice == "y":
    remove_index = int(input("\nWhich item you want to remove: "))
    numbers.remove(numbers[remove_index - 1])
    print(f"List after remove {remove_index} item")
    print(numbers)
else:
    print("\nList without remove any item:")
    print(numbers)
