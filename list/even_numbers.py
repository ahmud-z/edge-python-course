# Write a Python Program to get only Even Numbers from another List which Contains Numbers from 1 to 20 using List Comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = [num for num in numbers if (num % 2 == 0)]

print("List of Even Numbers: ")
print(even_numbers)
