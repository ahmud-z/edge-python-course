# sum of digits in a number

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    x = int(num % 10)
    sum = sum + x
    num = num / 10

print(f"Sum of the given number digits: {sum}")
