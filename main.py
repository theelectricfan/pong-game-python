import turtle
from boundary import Boundary
from centreline import CentreLine
from paddle import Paddle

screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(width=800, height=500)
screen.bgcolor("black")


boundary = Boundary()

centreLine = CentreLine()

paddle1= Paddle((-350, 0))
paddle2= Paddle((350, 0))
screen.update()

screen.exitonclick()