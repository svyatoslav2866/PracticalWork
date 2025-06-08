nums = [1, 10, 2, 3, -3, 4, -10, 8, -2]
positive_nums = []

for i in nums:
    if i > 0 and i % 2 == 0:
        positive_nums.append(i)
        positive_nums.sort()

print(positive_nums)