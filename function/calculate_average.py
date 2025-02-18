# Write a Python Program to Make an Average Calculator


def cal_avg(*nums):
    total_num = len(nums)
    sum = 0
    for i in nums:
        sum = sum + i

    return sum / total_num


print(f"Average of given numbers: {cal_avg(10,10,10)}")
