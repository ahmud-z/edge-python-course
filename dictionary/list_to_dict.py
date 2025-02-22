# Write a Python Program to Create a Dictionary from List which multiplies the values with 2 using Dictionary comprehension.

numbers = [1, 2, 3, 4, 5]

new_dict = {key: (key * 2) for (key) in numbers}

for key, value in new_dict.items():
    print(f"{key} : {value}")
