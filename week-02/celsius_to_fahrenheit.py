def celsius_fahrenheit(celsius_temparature):
    return (celsius_temparature * 9 / 5) + 32.0

def main():
    celsius_temparature = float(input("Enter your temparature(C): "))

    print(f"Given Temparature in Fahrenheit scale: {celsius_fahrenheit(celsius_temparature)} F")

main()