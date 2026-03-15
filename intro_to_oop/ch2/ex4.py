"""
Add a class method to your Car class that calculates and 
prints any car's average gas mileage (miles per gallon). 
You can compute the mileage by dividing the distance traveled 
(in miles) by the fuel burned (in gallons).



"""

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.ignition_status = 'off'

    @classmethod
    def gas_mileage(cls, miles, gallons):
        print(f"Your average gas mileage is {miles / gallons:.2f} miles per gallon")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    def spray_paint(self, color):
        self.color = color
        print(f"You just spray painted the car {color}! Rad!")

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
mustang.spray_paint("neon green")
mustang.gas_mileage(60, 3)