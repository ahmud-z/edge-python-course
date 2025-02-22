# Write a Python Program to Create a Dictionary from a List which Displays Length of those Word which Contain Greater than 5 Character as Value.

words = ["Day", "after", "tommorrow", "is", "sunday"]

words_lengths = {key: len(key) for (key) in words if (len(key) >= 5)}

print("\nWords with length 5 or upper:")
for key, value in words_lengths.items():
    print(f"{key} : {value}")
