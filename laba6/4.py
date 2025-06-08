nums = [-3, -2, -1, 0, 1, 2, 3]

first_nums = None
negative_nums = None

for i in nums:
    if i > 0 and first_nums is None:
        first_nums = i
    if i < 0:
        negative_nums = i

print("первый положительный элемент: ",first_nums)
print("последний отрицательный элемент: ",negative_nums)


