# sum number until negative number founr in a list

numbers = [1, 2, 7, -10, 2, -68, 52, 84]
sum = 0

for num in numbers:
    if num > 0:
        sum = sum + num
    else:
        break

print(sum)