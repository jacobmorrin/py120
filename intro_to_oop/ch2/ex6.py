"""
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.
You should have an instance variable that keeps track of the current speed. Initialize it 
to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. 
Each method should display an appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods.


"""
class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    
    @staticmethod
    def engine_on():
        print(f'Rev those engines! Your car is now on')
    
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

mustang = Car('Mustang', '1987', 'Azure')
print(mustang.model)
mustang.engine_on()
mustang.accelerate(10)
mustang.accelerate(100)
mustang.decelerate(100)