class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"I'm a cat! My name is {self.name}!")



kitty = Cat('Sophie')
kitty.greet()