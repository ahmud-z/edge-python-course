# Write a Python Program to Create a Dictionary which Displays Student Basic Information in the following format:
# Id : 10
# Name : Jafri
# Course : Python
# Address : ABC
# Contact : 1233454569

student = {
    "Id": 10,
    "Name": "Jafri",
    "Course": "Python",
    "Address": "ABC",
    "Contact": 1233454569,
}

print("\nStudent Details")
for key in student.keys():
    print(f"{key}: {student[key]}")
