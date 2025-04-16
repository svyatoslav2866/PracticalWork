class Counter:
    def realize_counter(self, counter):
        self.counter = counter

    def get_counter(self):
        print(self.counter)

    def increase(self):
        self.counter += 1
        return self.counter

    def decrease(self):
        self.counter -= 1
        return self.counter

    def set_value(self, value):
        self.counter = value
        return self.counter

counter = Counter()
counter.realize_counter(10)


while True:
    choice = int(input("\n выберите действие для счетчика: "
                       "\n 1 - вывести его показатель"
                       "\n 2 - увеличить на единицу"
                       "\n 3 - уменьшить на единицу"
                       "\n 4 - установить другое значение"
                       "\n 0 - выход"))

    match choice:
        case 1:
            counter.get_counter()
        case 2:
            print(f"увеличение счетчика на 1: {counter.increase()} ")
        case 3:
            print(f"уменьшение счетчика на 1: {counter.decrease()} ")
        case 4:
            new_value = int(input("Введите новое значение счетчика: "))
            print(f"Новое значение счетчика: {counter.set_value(new_value)}")
        case 0:
            break
