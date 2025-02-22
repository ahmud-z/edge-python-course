# Write a Python Program to Check Specific Key, whether that Key Exist in Dictionary or Not.

data = {"name": "Ahmud", "age": 23, "dept": "CSE"}

input_key = input("Enter a string key: ")

if data.get(input_key) != None:
    print("Key Exist in Dictionary")
    print(f"{input_key} : {data[input_key]}")
else:
    print("Key Dosen't Exist")
