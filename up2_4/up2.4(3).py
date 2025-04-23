import sqlite3
import psutil

conn = sqlite3.connect('datasystem.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS info(
    CPU INTEGER,
    memory INTEGER,
    disk INTEGER
    )
    ''')
    conn.commit()

def system_monitor():
    disk_us = psutil.disk_usage('C:\\')
    cpu_us = psutil.cpu_percent(interval=1)
    memory_us = psutil.virtual_memory().percent
    return cpu_us, memory_us, disk_us.percent
cpu, memory, disk = system_monitor()

def add_system_info():
    cursor.execute('''
    INSERT INTO info (CPU, memory, disk)
    VALUES (?, ?, ?) 
    ''', (cpu, memory, disk))
    conn.commit()

def main():
    create_table()
    while True:
        choice = int(input("\n1 - посмотреть системные данные, 0 - выход:"))

        match choice:
            case 1:
                print(f"использование CPU: {cpu}%")
                print(f"использование оперативной памяти: {memory}%")
                print(f"использование диска: {disk}%")
            case 2:
                print("программа завершила работу!")
                break

if __name__ == "__main__":
    main()

conn.close()