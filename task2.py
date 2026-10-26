import random

def get_numbers_ticket(min, max, quantity):
    numbers=[]
    try:
        if min<1 or max>1000 or (quantity<1 or quantity>1000):
            return list
        else:
            numbers=random.sample(range(min,max+1),quantity)
        
        return sorted(numbers)

    except TypeError:
        return "bad type"
    except ValueError:
        return numbers


print(get_numbers_ticket(0,5,3))
print(get_numbers_ticket(10,15,23))
print(get_numbers_ticket(1,5,3))
