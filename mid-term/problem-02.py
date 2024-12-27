# find largest and smallest number from a list of numbers

str_nums = input("Enter some integer numbers (separed by space): ")

num_list = str_nums.split(" ")

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

print(f"Largest number of given numbers: {max(num_list)}")
print(f"Smallest number of given numbers: {min(num_list)}")
