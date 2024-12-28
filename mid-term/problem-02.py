# find largest and smallest number from a list of numbers
numbers = input("Enter some integer numbers (separed by space): ")
numbers = numbers.split(" ")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(f"Largest number of given numbers: {max(numbers)}")
print(f"Smallest number of given numbers: {min(numbers)}")
