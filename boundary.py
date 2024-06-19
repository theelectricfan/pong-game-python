import turtle

class Boundary(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-400, 250)
        self.pendown()
        self.width(20)
        self.color('orange')
        for n in range(2):
            self.forward(800)
            self.right(90)
            self.forward(500)
            self.right(90)
