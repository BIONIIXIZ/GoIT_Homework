from random import randint , sample

def get_numbers_ticket(min, max,quantity):
    numbers = []
    for i in range(quantity):
        if min < 0 or max > 1000 or quantity > (max - min + 1):
            return []
        numbers.append(randint(min, max))
    return sorted(sample(range(min, max + 1), quantity))

lotery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:",lotery_numbers)
