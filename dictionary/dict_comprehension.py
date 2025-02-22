numbers = {
    "k1": 1,
    "k2": 2,
    "k3": 3,
    "k4": 4,
    "k5": 5,
    "k6": 6,
    "k7": 7,
    "k8": 8,
    "k9": 9,
    "k10": 10,
}

even_numbers = {key: value for (key, value) in numbers.items() if (value % 2 == 0)}
print(even_numbers.values())
