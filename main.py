import turtle
from boundary import Boundary
from centreline import CentreLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(width=800, height=500)
screen.bgcolor("black")

boundary = Boundary()
centreLine = CentreLine()
ball = Ball()
scoreboard = Scoreboard()
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))

# Dictionary to keep track of the state of each key
key_state = {
    "w": False,
    "s": False,
    "i": False,
    "k": False
}


# Functions to update key states
def update_key_state(key, state):
    key_state[key] = state


# Functions for paddle movements
def move_paddles():
    if key_state["w"]:
        paddle1.go_up()
    if key_state["s"]:
        paddle1.go_down()
    if key_state["i"]:
        paddle2.go_up()
    if key_state["k"]:
        paddle2.go_down()


# Key bindings using screen.onkeypress and screen.onkeyrelease
screen.listen()

screen.onkeypress(lambda: update_key_state("w", True), "w")
screen.onkeyrelease(lambda: update_key_state("w", False), "w")

screen.onkeypress(lambda: update_key_state("s", True), "s")
screen.onkeyrelease(lambda: update_key_state("s", False), "s")

screen.onkeypress(lambda: update_key_state("i", True), "i")
screen.onkeyrelease(lambda: update_key_state("i", False), "i")

screen.onkeypress(lambda: update_key_state("k", True), "k")
screen.onkeyrelease(lambda: update_key_state("k", False), "k")

game_on = True
# Main game loop
while game_on:
    ball.move(paddle1.position(), paddle2.position(), scoreboard)
    move_paddles()
    screen.update()
    if scoreboard.l_score == 5:
        game_on = False
    if scoreboard.r_score == 5:
        game_on = False

screen.exitonclick()
