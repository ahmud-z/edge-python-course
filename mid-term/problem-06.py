# separate even and odd numbers into two separate list

str_nums = input("Enter some integer numbers (separed by space): ")

numbers = str_nums.split(" ")
even_list = []
odd_list = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])

print(f"List of even numbers:{even_list}", end=" ")
print()
print(f"List of odd numbers:{odd_list}", end=" ")
