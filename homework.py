from datetime import datetime, date


def string_to_date(date_string):
    # Конвертуємо строку у datetime.date
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def get_days_from_today(inputing_date):
    try:
        # Отримуємо поточну дату
        todayd = date.today()

        if isinstance(inputing_date, str):
            # Якщо вхідне значення рядок, конвертуємо через func string_to_date
            inputing_date = string_to_date(inputing_date)

        elif isinstance(inputing_date, datetime):
            # Якщо це datetime, перетворюємо на дату
            inputing_date = inputing_date.date()

        # Обчислюємо різницю
        delta = todayd - inputing_date

        return delta.days

    except ValueError:
        return "Error"


# Приклад виклику функції
assert get_days_from_today(datetime(2022, 2, 24))  # Передаємо datetime
assert get_days_from_today("2022.2.24")  # Передаємо строку

print(get_days_from_today("2022.2.24"))
print(get_days_from_today(datetime(2022, 2, 24)))
