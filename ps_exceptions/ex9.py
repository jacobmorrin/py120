"""
Write two functions to fetch the sixth element from the list: 
one using the LBYL approach and another using the AFNP approach.
 In both cases, the function should return None when the element isn't found.

"""
numbers = [1, 2, 3, 4, 5]

def get_num_lbyl(lst):
    if len(lst) > 5:
        return lst[5]
    else:
        return None
    
def get_num_afnp(lst):
    try:
        return lst[5]
    except IndexError:
        return None

print(get_num_lbyl(numbers))
print(get_num_afnp(numbers))
