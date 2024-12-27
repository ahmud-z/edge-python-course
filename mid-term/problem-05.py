# find fibonacci inside a certain range
def find_fibo(num):
    term1 = 0
    term2 = 1
    print(term1, end=" ")
    print(term2, end=" ")
    while True:
        nextTerm = term1 + term2
        if nextTerm >= num:
            break
        print(nextTerm, end=" ")
        term1 = term2
        term2 = nextTerm


def main():
    num = int(input("Enter a number: "))
    find_fibo(num)


main()
