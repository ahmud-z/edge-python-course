# Write a Python Program to Get 5 Numbers from User and Create a Dictionary which Displays Square of Every Numbers as Value.

sqr_numbers = {}

print("\n")
for i in range(5):
    num = int(input(f"Enter number -{i+1} : "))
    sqr_numbers[num] = num * num


print("\nsquare of given number")
for key in sqr_numbers.keys():
    print(f"{key} : {sqr_numbers[key]}")
