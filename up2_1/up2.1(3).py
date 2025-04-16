nums = [1, 2, 3, 4, 2, 5, 6, 1, 5, 8]

def TrueNums(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
        else:
            return False

result = TrueNums(nums)
print(result)