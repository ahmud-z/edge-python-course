# find sum of even and odd numbers between two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

even_sum = 0
odd_sum = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(f"Sum of even numbers in given range: {even_sum}")
print(f"Sum of odd numbers in given range: {odd_sum}")
