# Write a Python Program to Get Color Name and its Code, and Display all the Color Name in Uppercase with their Code.

colors = {}

for i in range(3):
    c_name = input(f"Enter a color name (str): ")
    c_code = input(f"Enter it's color code: ")
    colors[c_name] = c_code


print("\nColor - Code")
for color, code in colors.items():
    print(f"{color.upper()} => {code}")
