class Integers:
    def __init__(self, num1=0, num2=0):
        self.number1 = num1
        self.number2 = num2

    def get_num(self):  # метод для вывода
        print(f"число 1: {self.number1}, число 2: {self.number2}")

    def change_number1(self, new_number1):
        self.number1 = new_number1

    def change_number2(self, new_number2):
        self.number2 = new_number2

    def sum_numbers(self):
        return self.number1 + self.number2

    def max_number(self):
        return max(self.number1, self.number2)


numbers = Integers(15, 20)

while True:
    choice = input("\nВыберите действие:\n"
                   "1 - вывести числа\n"
                   "2 - изменить числа\n"
                   "3 - вывести сумму чисел\n"
                   "4 - найти наибольшее число\n"
                   "0 - выход\n"
                   "Ваш выбор: ")

    match choice:
        case '1':
            numbers.get_num()

        case '2':
            num1 = int(input("Введите новое значение для числа 1: "))
            num2 = int(input("Введите новое значение для числа 2: "))
            numbers.change_number1(num1)
            numbers.change_number2(num2)
            print("Числа успешно изменены!")

        case '3':
            print(f"Сумма чисел: {numbers.sum_numbers()}")

        case '4':
            print(f"Наибольшее число: {numbers.max_number()}")

        case '0':
            print("Выход из программы...")
            break

        case _:
            print("Неверный выбор!")