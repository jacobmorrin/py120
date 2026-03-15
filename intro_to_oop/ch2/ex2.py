"""
Using decorators, add getter and setter methods to your Car class so you can 
view and change the color of your car. You should also add getter methods that 
let you view but not modify the car's model and year. Don't forget to write some tests.

"""

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.ignition_status = 'off'

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    def engine_on(self):
        self.ignition_status = 'on'
        print(f'Rev those engines! Your car is now {self.ignition_status}')
    
    def engine_off(self):
        self.ignition_status = 'off'
        self.speed = 0
        print(f'You just turned the engine off!')
    
    def accelerate(self, number):
        self.speed += number
        print(f'You just accelerated. Your current speed is {self.speed}')

    def decelerate(self, number):
        self.speed -= number
        print(f'You just hit the brakes. Your current speed is {self.speed}')
    
    def get_speed(self):
        print(f'Your speed is {self.speed} mph.')

mustang = Car('Mustang', '1987', 'Blue')
print(mustang.color)
mustang.color = "red"
print(mustang.color)
