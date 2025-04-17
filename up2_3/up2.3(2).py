class Worker:

    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_rate(self):
        return self.__rate
    def get_days(self):
        return self.__days

    def get_data(self):
        print(f"{self.__name} {self.__surname}, rate: {self.__rate}, days: {self.__days}")

    def GetSalary(self):
        return self.__rate * self.__days

worker1 = Worker("имя: Evgeny","фамилия: Pupkin",  5000, 20)
worker2 = Worker("имя: Dmitry","фамилия: Vasilev", 4500, 15)
worker3 = Worker("имя: George","фамилия: Petrov", 7000, 24)


while True:
    choice = int(input("\nвыберите действие: "
                       "\n1 - вывести работника 1"
                       "\n2 - вывести работника 2"
                       "\n3 - вывести работника 3"
                       "\n4 - вывести всех работников"
                       "\n5 - вывести их зарпалту за месяц"
                       "\n6 - выход из программы"))

    match choice:
        case 1:
            worker1.get_data()
        case 2:
            worker2.get_data()
        case 3:
            worker3.get_data()
        case 4:
            worker1.get_data()
            worker2.get_data()
            worker3.get_data()
        case 5:
            print(f"зарплата работника Evgeny за месяц: {worker1.GetSalary()}")
            print(f"зарплата работника Dmitry за месяц: {worker2.GetSalary()}")
            print(f"зарплата работника George за месяц: {worker3.GetSalary()}")
        case 6:
            break
        case _:
            print("неверный выбор!")