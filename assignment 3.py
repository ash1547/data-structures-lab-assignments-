class Shape:
    def draw(self):
        print("Drawing a Shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

s1 = Circle()
s2 = Rectangle()

s1.draw()
s2.draw()
