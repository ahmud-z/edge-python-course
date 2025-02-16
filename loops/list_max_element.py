# find the max element from a list

numbers = [5, 4, 26, 9, 56, 83, 42, 43, 56, 74]
maxElement = numbers[0]

for num in numbers:
    if num > maxElement:
        maxElement = num

print(f"Max element of given list: {maxElement}")
