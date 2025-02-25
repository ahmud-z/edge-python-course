# Write a Python Program to Get Only Students Name with Ending Character ‘a’ from a SET of Students using SET Comprehension.

student_names = {"ahmud", "nuzaifa", "nabhan"}

names_endswith_a = {name for name in student_names if name.endswith("a")}

print("\nAll Students Name__")
print(student_names)

print("\n Student names ends with 'a")
print(names_endswith_a)
