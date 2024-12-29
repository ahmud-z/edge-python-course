# swap two variable without using a third variable.

def swap(a, b):
    return b, a


def main():
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))
    number1, number2 = swap(number1, number2)

    print(
        f"\nAfter swap:\nFirst Number: {round(number1)}\nSecond Number: {round(number2)}"
    )

main()