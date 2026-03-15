class Cat:
    COLOR = 'purple'

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {self.__class__.COLOR} cat!")

kitty = Cat('Sophie')
kitty.greet()