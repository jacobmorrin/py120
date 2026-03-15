"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two 
objects from that class. The class should have at least 
one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies 
the above requirements.


"""

class PlayerCharacter:

    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

    def attack(self):
        print(f'{self.name} attacks! Hiya!')

    def defend(self):
        print(f'{self.name} defends! En guard!')

class Mage(PlayerCharacter):

    def cast_spell(self):
        print(f'{self.name} casts a spell!')

class Warrior(PlayerCharacter):

    def swings_axe(self):
        print(f'{self.name} swings axe!')