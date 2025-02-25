# Write a Python Program to Get Only Odd Numbers from 100 Generated number using Set Comprehension.

odd_numbers = set()

odd_numbers = {num for num in range(1, 101) if num % 2 != 0}

print("Odd Numbers set between 1 to 100__ ")
print(odd_numbers)
