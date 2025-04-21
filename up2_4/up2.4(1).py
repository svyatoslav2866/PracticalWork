import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    group_name TEXT,
    grade1 INTEGER,
    grade2 INTEGER,
    grade3 INTEGER,
    grade4 INTEGER
)
""")
conn.commit()


def add_student():
    print("\nДобавьте нового студента:")
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    group = input("Группа: ")

    print("Введите 4 оценки через пробел: ")
    grades = list(map(int, input().split()))

    cursor.execute("""
    INSERT INTO students (name, surname, patronymic, group_name, grade1, grade2, grade3, grade4)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, surname, patronymic, group, *grades))
    conn.commit()
    print("Студент добавлен\n")


def show_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("Нет студентов в базе!")
        return

    print("\nСписок всех студентов:")
    for student in students:
        avg = sum(student[5:9]) / 4
        print(f"ID: {student[0]}, {student[2]} {student[1]} {student[3]}, Группа: {student[4]}")
        print(f"Оценки: {student[5:9]}, Средний балл: {avg:.1f}\n")


def show_student():
    student_id = input("Введите ID студента: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        avg = sum(student[5:9]) / 4
        print(f"\nID: {student[0]}")
        print(f"ФИО: {student[2]} {student[1]} {student[3]}")
        print(f"Группа: {student[4]}")
        print(f"Оценки: {student[5:9]}")
        print(f"Средний балл: {avg:.1f}\n")
    else:
        print("Студент не найден")


def edit_student():
    student_id = input("Введите ID студента для редактирования: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Студент не найден")
        return

    print("\nТекущие данные:")
    print(f"1. Имя: {student[1]}")
    print(f"2. Фамилия: {student[2]}")
    print(f"3. Отчество: {student[3]}")
    print(f"4. Группа: {student[4]}")
    print(f"5. Оценки: {student[5:9]}")

    field = input("\nЧто хотите изменить? 1-5, 0 для отмены: ")

    if field == '0':
        return

    if field in ['1', '2', '3', '4']:
        new_value = input("Введите новое значение: ")
        fields = ['name', 'surname', 'patronymic', 'group_name']
        cursor.execute(f"UPDATE students SET {fields[int(field) - 1]} = ? WHERE id = ?",
                       (new_value, student_id))
    elif field == '5':
        print("Введите 4 новые оценки через пробел:")
        grades = list(map(int, input().split()))
        cursor.execute("""
        UPDATE students 
        SET grade1 = ?, grade2 = ?, grade3 = ?, grade4 = ?
        WHERE id = ?
        """, (*grades, student_id))

    conn.commit()
    print("Изменения сохранены")


def delete_student():
    student_id = input("Введите ID студента для удаления: ")

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Студент удален")
    else:
        print("Студент не найден")


def group_average():
    group = input("Введите название группы: ")

    cursor.execute("""
    SELECT grade1, grade2, grade3, grade4 
    FROM students WHERE group_name = ?
    """, (group,))

    grades = []
    for row in cursor.fetchall():
        grades.extend(row)

    if grades:
        avg = sum(grades) / len(grades)
        print(f"\nСредний балл группы {group}: {avg:.2f}\n")
    else:
        print("Группа не найдена или нет студентов")


def main():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить студента")
        print("2 - Показать всех студентов")
        print("3 - Найти студента по ID")
        print("4 - Редактировать студента")
        print("5 - Удалить студента")
        print("6 - Средний балл группы")
        print("0 - Выход")

        choice = input(": ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            show_student()
        elif choice == '4':
            edit_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            group_average()
        elif choice == '0':
            conn.close()
            print("Программа завершена")
            break
        else:
            print("Неверный ввод, попробуйте снова")


if __name__ == "__main__":
    main()