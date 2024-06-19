import turtle

class CentreLine(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.goto(0, -245)
        self.pendown()
        self.left(90)
        for i in range(25):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()