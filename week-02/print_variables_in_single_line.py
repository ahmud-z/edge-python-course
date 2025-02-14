# Take the sentence: All work and no play makes Jack a dull boy. Store ech word in a separate variable, then print out the sentence on one line using print.

sentence = input("Enter your senentence: ")

words = sentence.split(" ")

for word in words:
    print(f"{word} ", end="")
