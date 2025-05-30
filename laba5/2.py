nums = [-1, -2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_nums(nums):
    total_sum = sum(num for num in nums if num > 0)

    min_num = min(nums)
    max_num = max(nums)
    min_index = nums.index(min_num)
    max_index = nums.index(max_num)

    begin = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    total = 1
    for num in nums[begin:end]:
        total *= num

    return total_sum, total

result = sum_nums(nums)
print(result)