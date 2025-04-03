import re

def  normalize_phone(phone_numbers):
    normalized = []
    [re.sub(r"\s", "", i) for i in phone_numbers]
    for numbers in phone_numbers:
        numbers = re.sub(r"\s", "", numbers)
        if re.match(r"^\+38\d{10]$", numbers) or re.match(r"^380\d{9}$", numbers):
            normalized.append(numbers)
        elif re.match("r^\{10}$", numbers):
            normalized.append("+38" + numbers)
        elif re.match("r^\{9}$", numbers):
            normalized.append("+380" + numbers)
        elif re.match(r"^\(?\d{3}\)?\d{7}$", numbers):
            number = re.sub(r"[()]", "", numbers)  # Видаляємо дужки
            normalized.append("+38" + number)
        else:
            normalized.append(numbers)


    return normalized


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

c_phone_numbers = normalize_phone(phone_numbers)

print(c_phone_numbers)
