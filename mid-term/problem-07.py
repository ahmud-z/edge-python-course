# remove duplicates numbers from a list
def remove_duplicate(numbers):
    return list(dict.fromkeys(numbers))


def main():
    numbers = input("Enter some integer numbers (separed by space): ")
    numbers = numbers.split(" ")

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    print(remove_duplicate(numbers))


main()
