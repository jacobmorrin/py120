"""
Create a Person class with a "private" attribute _name. 
Use properties to create a getter and setter for the 
_name attribute. The _name attribute must be a string. 
Be sure to test your code.

"""

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Please enter a valid name.')
        
        if name.strip() == '':
            raise ValueError('Blank names are not allowed!')
        
        self._name = name

bob = Person('bob')
print(bob.name)
bob.name = 'Frank'
print(bob.name)
bob.name = '5'
bob.name = '     '