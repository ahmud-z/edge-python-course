# Write a Python Program to get only Students Name with starting Character ‘a’ From a Complete List of Students using List Comprehension.

student_names = ["ahmud", "bob", "nabhan", "sojib", "john", "tanim", "mahmud", "soyket"]

special_names = [name for name in student_names if ("a" in name)]

print("List of names that contains character 'a':")
print(special_names)
