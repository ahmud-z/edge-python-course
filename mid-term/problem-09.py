# count total no of vowel and consonant from a string

sentence = input("Enter a string: ")
vowel = 0
consonant = 0

for i in sentence:
    if (
        i == "a"
        or i == "e"
        or i == "i"
        or i == "o"
        or i == "u"
        or i == "A"
        or i == "E"
        or i == "I"
        or i == "O"
        or i == "U"
    ):
        vowel = vowel + 1
    else:
        consonant = consonant + 1

print(f"Total vowel in given text: {vowel}")
print(f"Total consonant in given text: {consonant}")
