class Fitness:

    def __init__(self, ID, years, month_number, session_duration):
        self.ID = ID
        self.years = years
        self.month_number = month_number
        self.session_duration = session_duration


sessions = [
    Fitness("1", 2025, 4, 60),
    Fitness("2", 2025, 1, 45),
    Fitness("3", 2025, 6, 90),
    Fitness("4", 2025, 5, 60),
    Fitness("5", 2025, 3, 30),
    Fitness("6", 2024, 4, 70),
    Fitness("7", 2024, 1, 45),
    Fitness("8", 2024, 6, 90),
    Fitness("9", 2024, 5, 60),
    Fitness("10", 2024, 3, 40)
]


def find_most_active_year():
    year_stats = {}

    for session in sessions:
        if session.years in year_stats:
            year_stats[session.years] += session.session_duration
        else:
            year_stats[session.years] = session.session_duration

    max_duration = max(year_stats.values())

    max_years = [year for year, duration in year_stats.items() if duration == max_duration]

    best_year = min(max_years)

    print(f"\nГод с наибольшей суммарной продолжительностью: {best_year}")
    print(f"Суммарная продолжительность занятий в этом году: {year_stats[best_year]} минут")

find_most_active_year()