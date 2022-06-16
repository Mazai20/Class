class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle:{self.x},{self.y},{self.height},{self.width}"
    def get_area(self):
        return self.width * self.height

reac = Rectangle(5, 10, 50, 100)
print(reac)
print(reac.get_area())