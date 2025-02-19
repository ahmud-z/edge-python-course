# Write a Python Program to get 10 Numbers from the user. Display Number that Less than 20 and Greater than 10.

print("Enter 5 numbers one by one: ")
numbers = []

for i in range(5):
    num = int(input())
    numbers.append(num)


print("\nNumber that are greater than 10 and less than 20:")
for num in numbers:
    if num > 10 and num < 20:
        print(num)
