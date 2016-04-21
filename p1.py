def average_num(nums):
    total_nums = 0
    N = float(len(nums))
    for num in nums:
        total_nums += num

    return total_nums/N


integer_array = [80, 19, 20, 22, 100, 14, 19, 22]
result = average_num(integer_array)
print "Averrage: ", result