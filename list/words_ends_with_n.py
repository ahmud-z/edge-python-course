# Write a Python Program to get  5 words from user, display that word which ends with ‘n’ character.


sentence = input("Enter a sentence: ")
sentence = sentence.lower()

words = sentence.split(" ")

print("\nWords that ends with 'n': ")

for word in words:
    if word.endswith("n"):
        print(word)
