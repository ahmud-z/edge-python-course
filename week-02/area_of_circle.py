# Calculate the area of a circle using the formula area = PI * radius^2.

PI = 3.1415

def calculate_area(radius):
    return PI * (radius * radius)


def main():
    radius = float(input("Enter your circle radius: "))
    print(f"Calculated Area: {round(calculate_area(radius), 2)}")


main()
