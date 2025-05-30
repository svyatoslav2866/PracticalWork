a = int(input("введите число a: "))
b = int(input("введите число b: "))

def expression(a, b):
    result = (a + 4 ** b) * (a - 3 ** b) + a * 2
    return result

print(expression(a, b))