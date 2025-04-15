def combination(arr, target):
    result = []

    def back(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(arr)):

            path.append(arr[i])
            back(i + 1, path, remaining - arr[i])
            path.pop()

    back(0, [], target)
    return result


arr = [1, 2, 5, 6, 8, 3]
target = int(input("введите цель: "))
print(combination(arr, target))
