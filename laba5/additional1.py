class Car:

    def __init__(self, stamp, model, years):
        self.stamp = stamp
        self.model = model
        self.years = years

    def print_car(self):
        print(self.stamp, self.model, self.years)


Car1 = Car("BMW", "X6", 2022)
Car2 = Car("Porshe", "911", 2023)
Car3 = Car("Mersedes", "cls 63", 2019)

Car1.print_car()
Car2.print_car()
Car3.print_car()