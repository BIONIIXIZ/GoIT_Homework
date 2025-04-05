from datetime import datetime, date

def get_days_from_today(inputing_date):
    try:

        c_date = datetime.strptime(inputing_date, "%Y-%m-%d").date()


        # Отримуємо поточну дату
        todayd = date.today()

        # Обчислюємо різницю

        delta = todayd - c_date

        return delta.days

    except ValueError:
        return None


# Приклад виклику функції
print(get_days_from_today("2021-10-09"))  # Результат: кількість днів залежить від сьогоднішньої дати
print(get_days_from_today("2023-01-01"))  # Результат: кількість днів можливо від'ємне число
print(get_days_from_today("incorrect format!"))  # None
