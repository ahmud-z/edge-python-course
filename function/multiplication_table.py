# Write a Python Program to get a Number from User to Display Multiplication Table for that Number in Reverse Mode

def reverse_multiplication_table(number):
    print(f"Reversed Multiplication Table of {number}")
    for i in range(10, 0, -1):
        print(f"{number}X{i} = {(number*i)}")


reverse_multiplication_table(5)
