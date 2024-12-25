def is_palindrome(str):
    temp = str
    return "".join(reversed(str)) == temp


def main():
    str = input("Enter a string: ")
    if is_palindrome(str):
        print("Palindrome")
    else:
        print("Not Palindrome")


main()
