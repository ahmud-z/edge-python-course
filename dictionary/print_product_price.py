# Write a Python Program to Get 5 Digital Product and their Price. Display Total Price of the Products.

products = {}

for i in range(2):
    name = input(f"Enter product{i+1} name(string): ")
    price = int(input(f"Enter product{i+1} price: "))
    products[name] = price


print("Products names with price:")
for name, price in products.items():
    print(f"{name} : {price}")
