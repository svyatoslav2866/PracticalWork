class Task:

    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

    def get_date(self):
        return self.DateStart, self.DateFinish, self.Description

tasks = [
    Task("2025-06-01 09:00", "2025-06-01 10:30", "Утреннее совещание"),
    Task("2025-06-01 11:00", "2025-06-01 13:00", "Работа над проектом"),
    Task("2025-06-01 14:00", "2025-06-01 15:30", "Презентация"),
    Task("2025-06-01 16:00", "2025-06-01 18:00", "Анализ данных"),
    Task("2025-06-01 17:00", "2025-06-01 19:00", "Встреча с клиентом")
]

latest_task = min(tasks, key=lambda x: x.DateFinish)

print(f"самая поздняя задача: {latest_task.get_date()}")