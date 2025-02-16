# count digits until a specific digit is found


num = input("Enter a number: ")
totalDigits = len(num) - 1

num = int(num)

targetDigit = int(input("Enter a digit you want to search: "))

count = 0

while num > 0:
    digit = int(num / pow(10, totalDigits))
    num = num - (digit * pow(10, totalDigits))
    totalDigits = totalDigits - 1

    if digit == targetDigit:
        break

    count = count + 1

print(f"Total digit count is [{count}] before the target digit: {targetDigit}")

