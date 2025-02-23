# Write a Python Program to Get 5 Numbers from User to Store in a Set to Find their Addition and Product.

numbers = set()
sum = 0
mul = 1
inp = input("Enter 5 number separated by space: ")

inp = inp.split()

for i in inp:
    if i != "":
        numbers.add(int(i))
        sum = sum + int(i)
        mul = mul * int(i)

print("\n Given Set Items__")
print(numbers)


print(f"\nSum of set elements: {sum}")
print(f"Multiplication of set elements: {mul}")
