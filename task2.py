import random

def get_numbers_ticket(min, max, quantity):
    numbers=[]
    try:
        if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > max - min + 1:
            return []
        else:
            numbers=random.sample(range(min,max+1),quantity)

        return sorted(numbers)

    except TypeError:
        return "bad type"


print(get_numbers_ticket(1,5,3))
print(get_numbers_ticket(10,15,23))
print(get_numbers_ticket(1,10,3))
