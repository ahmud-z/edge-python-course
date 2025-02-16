# find the first negative number of a list

myList = [5, 46, -20, 5, -4, 2, -5, 4]

firstNegative = 0

for i in myList:
    if i < firstNegative:
        firstNegative = i
        break

print(f"First negative number of given list: {firstNegative}")
