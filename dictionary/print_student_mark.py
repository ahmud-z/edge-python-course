# Write a Python Program to Get 5 Student Name with their Marks and Display Student Name and their Marks in Key Value Form.

student_marks = {
    "John": 42,
    "Bob": 56,
    "Tom": 65,
    "Chad": 85,
    "Thomas": 78,
}

print("Name -- Marks")
for key, value in student_marks.items():
    print(f"{key} -- {value}")
