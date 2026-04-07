class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
rec1 = Rectangle(2, 3)
print(rec1.width)
print(rec1.length)
rec1.length = 1

