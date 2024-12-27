# find factorial of a number
def find_factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    return fact


def main():
    num = int(input("Enter a number: "))
    print(f"Factorial of given number: {find_factorial(num)}")


main()
