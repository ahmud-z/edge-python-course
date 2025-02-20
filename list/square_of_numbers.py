# Write a Python Program to get 5 integer numbers from user and store in a list, display that number using for loop, every number should display with its square.

str_nums = input("Enter some number (separated by single space): ")
str_nums = str_nums.split(" ")

for i in range(len(str_nums) - 1, 0, -1):
    if str_nums[i].isnumeric():
        break
    else:
        str_nums.pop()

numbers = []

for num in str_nums:
    numbers.append(int(num))

print("\nGiven List of Numbers: ")
print(numbers)

print("\n")
for i in numbers:
    print(f"Square of {i} is: {i * i}")
