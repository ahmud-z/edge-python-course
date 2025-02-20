# Write a Python Program in which user is able to modify any item of list.

nums = input("Enter some numbers(separated by space): ")
str_numbers = nums.split(" ")

numbers = []

for i in str_numbers:
    numbers.append(int(i))

print("\nGiven List of Numbers: ", end="")
print(numbers)


choice = input("\nAre you want to modify any item? (y/n): ")

if choice == "y":
    modify_index = int(input("\nWhich item you want to modify: "))
    input_value = input("Enter your input you want assign: ")
    numbers[modify_index - 1] = input_value
    print(f"Updated List after modify {modify_index-1} item")
    print(numbers)
else:
    print("\nList without remove any item:")
    print(numbers)
