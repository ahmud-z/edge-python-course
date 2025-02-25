# Write a Python Program to Get Items from user to Create Two Sets and Display all the Items from Both Sets Except Duplicate Items.

inp1 = input("Enter  set1 elements(separated by space): ")
inp2 = input("Enter set2 elements(separated by space): ")

inp1 = inp1.split(" ")
inp2 = inp2.split(" ")

set1 = {item for item in inp1 if item != " "}
set2 = {item for item in inp2 if item != " "}

print("Unique items from both sets: ")
print(set1.union(set2))
