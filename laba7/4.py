class Fitness:

    def __init__(self, ID, years, month_number, session_duration):
        self.ID = ID
        self.years = years
        self.month_number = month_number
        self.session_duration = session_duration

    def get_info(self):
        print(self.ID, self.years, self.month_number, self.session_duration)


sessions = [
    Fitness("1", 2025, 4, 60),
    Fitness("2", 2025, 1, 45),
    Fitness("3", 2025, 6, 90),
    Fitness("4", 2025, 5, 60),
    Fitness("5", 2025, 3, 30)
]

def print_shortest():
    shortest = min(sessions, key=lambda x: x.session_duration)
    shortest.get_info()

def print_longest():
    longest = max(sessions, key=lambda x: x.session_duration)
    longest.get_info()

while True:
    choice = int(input("\nвведите 1 что бы вывести самое короткое занятие"
                     "\nввведите 2 что бы вывести самое длинное занятие"
                     "\n3 - завершение работы программы"))

    match choice:
        case 1:
            print("Самое короткое занятие: ")
            print_shortest()
        case 2:
            print("Самое длинное занятие: ")
            print_longest()
        case 3:
            break