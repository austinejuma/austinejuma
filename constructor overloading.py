class Rectangle:
    def __init__(self, width, height=None):
        if height is None:  # Square case
            self.width = self.height = width
        else:  # Rectangle case
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

# Testing squares and rectangles
square = Rectangle(5)
rectangle = Rectangle(4, 6)
print(f"Area of square: {square.area()}")
print(f"Area of rectangle: {rectangle.area()}")
