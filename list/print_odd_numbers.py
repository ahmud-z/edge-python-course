# Write a Python Program to get 10 Numbers from user, Store in List, and Display only Odd Numbers getting from the List.

user_input = input("Enter some numbers separated by space: ")
numbers = []


for i in user_input.split(" "):
    numbers.append(int(i))


print("Odd Numbers from given")
for number in numbers:
    if number % 2 == 1:
        print(number)
