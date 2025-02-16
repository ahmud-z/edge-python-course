# print a multiplication table of a number up to 10

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} X {i} = {(number*i)}")
