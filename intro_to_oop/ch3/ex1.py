"""
Create a Car class that makes the following code work as indicated:

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')


"""


class Car:

    def __init__(self, id, year, color):
        self.id = id
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.color.capitalize()} {self.year} {self.id}'
    
    def __repr__(self):
        return f'Car({repr(self.color)}, {repr(self.year)}, {repr(self.id)})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
