import random   

def get_number_tickets(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers
lottery_numbers = get_number_tickets(1, 49, 6)
print("Ващі лотерейні числа:", lottery_numbers)
    