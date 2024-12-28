# find the longest word in a sentence
sentence = input("Enter some words(seprared by space): ")
words = sentence.split(" ")
max_word_len = -1

for i in range(0, len(words)):
    if len(words[i]) > max_word_len:
        max_word_len = len(words[i])
        max_word_index = i

print(f"Max length word: {words[max_word_index]}")
print(f"Length: {max_word_len}")
