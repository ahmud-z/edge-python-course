# Write a Python Program to Create a Numeric Dictionary which Displays only those Keys which have Even Value.

numbers = {
    "num1": 1,
    "num2": 10,
    "num3": 6,
    "num4": 7,
    "num5": 5,
    "num6": 61,
    "num7": 541,
}

print("\nEven Dict Items")
for key, value in numbers.items():
    if value % 2 == 0:
        print(f"{key} : {value}")
