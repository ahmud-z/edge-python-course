# Write a Python Program to get 3 Numbers from User to Find Greatest Number


def find_largest(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > z:
        return y
    else:
        return z


print(f"Largest Number: {find_largest(56,15,121)}")
