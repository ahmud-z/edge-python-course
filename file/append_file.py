# Modify the previous program to append the following line to data.txt:
# Line 4: This line is appended.

try:
    with open("data.txt", "a") as file:
        file.write("\nThis line is appended.")
        print("New data appended successfully!")

except:
    print("File not Found")
