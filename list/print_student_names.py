# Write a Python Program to get 5 Students Name from user and Store in List, Display all the Students Name with Uppercase Letters.

studnet_names = []

for i in range(5):
    name = input(f"Enter student name 0{i+1}: ")
    studnet_names.append(name)


for name in studnet_names:
    print(name.upper())