# Write a Python program that reads the contents of data.txt and prints each line with its corresponding line number.

count = 1

try:
    with open("data.txt", "r") as file:
        for line in file:
            print(f"{count}. {line}")
            count = count + 1
except:
    print("Given not exixt.")
