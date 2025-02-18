# Write a Python Program to get a Sentence from User, And Display Character of that Sentence that Present on Odd Index Number

sentence = input("Enter a sentence: ")

print("odd indexed characters: ")
for index in range(len(sentence)):
    if index % 2 == 0:
        print(sentence[index])
