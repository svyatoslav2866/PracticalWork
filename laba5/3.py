import random
nums = []
for i in range(20):
    val = random.randint(2, 20)
    if val % 2 == 0:
        nums.append(val)
nums.sort()
print(nums)