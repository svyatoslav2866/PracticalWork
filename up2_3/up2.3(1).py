class Worker:

    def __init__(self):
        self.rate = 0
        self.days = 0

    def info(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_worker(self):
        print(self.name, self.surname, self.rate, self.days)


    def GetSalary(self):
        return self.rate * self.days




worker1 = Worker()
worker1.info("имя: Evgeny","фамилия: Pupkin",  5000, 20)
worker2 = Worker()
worker2.info("имя: Dmitry","фамилия: Vasilev", 4500, 15)
worker3 = Worker()
worker3.info("имя: George","фамилия: Petrov", 7000, 24)


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
            worker1.get_worker()
        case 2:
            worker2.get_worker()
        case 3:
            worker3.get_worker()
        case 4:
            worker1.get_worker()
            worker2.get_worker()
            worker3.get_worker()
        case 5:
            print(f"зарплата работника Evgeny за месяц: {worker1.GetSalary()}")
            print(f"зарплата работника Dmitry за месяц: {worker2.GetSalary()}")
            print(f"зарплата работника George за месяц: {worker3.GetSalary()}")
        case 6:
            break
        case _:
            print("неверный выбор!")