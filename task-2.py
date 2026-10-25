import random

def get_numbers_ticket(min, max, quantity):
    list=[]
    try:
        if min<1 or max>1000 or (quantity<1 or quantity>1000):
            return list
        else:
            list=random.sample(range(min,max+1),quantity)
        
        return print(sorted(list))

    except TypeError:
        return "bad type"


print(get_numbers_ticket(0,5,3))
print(get_numbers_ticket(1,5,3))
