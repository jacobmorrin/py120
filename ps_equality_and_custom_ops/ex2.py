"""

"""

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()
    
fluffy = Cat('fluffy')
mr_meow = Cat('Mr. Meow')
good_cat = Cat('Fluffy')

print(fluffy == mr_meow)
print(good_cat == fluffy)