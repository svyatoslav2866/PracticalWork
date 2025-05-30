a = int(input("введите число: "))

def sum_num(a):
    if a > 1:
        return sum(range(1, a + 1))
    if a < 1:
        return sum(range(a, 1 + 1))

print(f"сумма чисел от 1 до {a} = {sum_num(a)}")