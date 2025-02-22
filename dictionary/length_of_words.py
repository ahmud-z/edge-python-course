# Write a Python Program to Create a Dictionary from a List which Displays Length of Each Word as Value.

words = ["Today", "is", "Friday"]

words_lengths = {key: len(key) for (key) in words}

print("\nWords with their Length")
for key, value in words_lengths.items():
    print(f"{key} : {value}")
