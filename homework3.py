import re


def normalize_phone(phone_number):
    """
    Функція нормалізує лише один номер телефону.
    """
    phone_number = re.sub(r"\s|-", "", phone_number)  # Видаляємо пробіли та дефіси

    if re.match(r"^\+38\d{10}$", phone_number) or re.match(r"^380\d{9}$", phone_number):
        # if number вже у правильному форматі
        return phone_number
    elif re.match(r"^\d{10}$", phone_number):
        # if номер у форматі 10 цифр
        return "+38" + phone_number
    elif re.match(r"^\d{9}$", phone_number):
        # if номер у форматі 9 цифр
        return "+380" + phone_number
    elif re.match(r"^\(?\d{3}\)?\d{7}$", phone_number):
        # if номер у форматі (XXX)XXXXXXX
        phone_number = re.sub(r"[()]", "", phone_number)  # Видаляємо дужки
        return "+38" + phone_number
    else:
        # Повертаємо номер у початковому вигляді, якщо він не відповідає жодним правилам
        return phone_number


phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "         50-592-12-51",
    "050-592-12-51    ",
    "  380-50-592-12-51 "
]

#Форматування тільки одного номера за індексом [0]
formatted_number = normalize_phone(phone_numbers[0])
print(f"Відформатований номер: {formatted_number}")
