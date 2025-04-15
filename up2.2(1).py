class Student:
    def __init__(self):
        self.surname = ""
        self.data_of_birth = ""
        self.number_group = ""
        self.grade = []

    def info(self, surname, data_of_birth, number_group, grade):
        self.surname = surname
        self.data_of_birth = data_of_birth
        self.number_group = number_group
        self.grade = grade

    def get_data(self):
        print(self.surname, self.data_of_birth, self.number_group, self.grade)

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birth(self, new_birth):
        self.data_of_birth = new_birth

    def change_group(self, new_group):
        self.number_group = new_group


Student1 = Student()
Student1.info("Светлов", "01.01.2005", "гр - 103", [4, 4, 5, 3, 5])
Student2 = Student()
Student2.info("Царев", "19.06.2006", "гр - 643", [5, 5, 5, 5, 5])
Student3 = Student()
Student3.info("Дудкин", "12.08.2006", "гр - 243", [3, 3, 4, 4, 5])
Student4 = Student()
Student4.info("Пряников", "04.02.2004", "гр - 140", [4, 5, 3, 4, 5])
Student5 = Student()
Student5.info("Безденежных", "26.12.2005", "гр - 541", [2, 3, 3, 4, 3])

while True:
    choice = int(
        input("\nчтобы вывести студента, введите его номер (до 5-ти) или 6 для вывода всех студентов, 0 - стоп: "))

    match choice:
        case 1:
            selected_student = Student1
        case 2:
            selected_student = Student2
        case 3:
            selected_student = Student3
        case 4:
            selected_student = Student4
        case 5:
            selected_student = Student5
        case 6:
            Student1.get_data()
            Student2.get_data()
            Student3.get_data()
            Student4.get_data()
            Student5.get_data()
            continue
        case 0:
            break
        case _:
            print("Неверный номер студента.")
            continue

    selected_student.get_data()

    action = int(input("выберите действие:\n"
                       "1 - сменить фамилию,\n"
                       "2 - изменить дату рождения,\n"
                       "3 - изменить номер группы,\n"
                       "4 - вывести данные\n"))

    match action:
        case 1:
            new_surname = input("введите новую фамилию: ")
            selected_student.change_surname(new_surname)
        case 2:
            new_birth = input("введите новую дату рождения: ")
            selected_student.change_birth(new_birth)
        case 3:
            new_group = input("введите новый номер группы: ")
            selected_student.change_group(new_group)
        case 4:
            selected_student.get_data()