class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_value(self, value):
        self.__balance += value
        return self.__balance

    def take_balance(self, value):
        self.__balance -= value
        return self.__balance

    def get_data(self):
        print(f"Ваш баланс: {self.__balance} рублей")


balance = BankAccount(2000)


while True:
    choice = int(input("\nВыберите действие: "
                       "\nПроверить баланс - 1"
                       "\nПополнить баланс - 2"
                       "\nСнять с баланса - 3"
                       "\nВыход из программы - 4"))

    match choice:
        case 1:
            balance.get_data()

        case 2:
            new_value = int(input("Введите сумму, которую хотите закинуть на баланс: "))
            print(f"Новое значение баланса: {balance.set_value(new_value)}")

        case 3:
            take = int(input("Введите сумму, которую хотите снять с баланса: "))
            print(f"Новое значение баланса: {balance.take_balance(take)}")

        case 4:
            print("Программа завершила работу!")
            break