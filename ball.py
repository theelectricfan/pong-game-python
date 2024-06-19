from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 0.07
        self.y_move = 0.07
        self.move_speed_factor = 1

    def move(self, paddle1_position, paddle2_position, scoreboard):
        new_x = self.xcor() + self.x_move * self.move_speed_factor
        new_y = self.ycor() + self.y_move * self.move_speed_factor
        self.goto(new_x, new_y)
        self.collision(paddle1_position, paddle2_position, scoreboard)

    def collision(self, paddle1_position, paddle2_position, scoreboard):
        if self.ycor() > 230 or self.ycor() < -230:
            self.bounce_y()

        if self.xcor() > 380:
            scoreboard.l_point()
            self.reset_position()

        if self.xcor() < -380:
            scoreboard.r_point()
            self.reset_position()

        if self.distance(paddle1_position) <= 61 and -340 >= self.xcor() >= -350:
            self.bounce_x()

        if self.distance(paddle2_position) <= 61 and 340 <= self.xcor() <= 350:
            self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed_factor *= 1.1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed_factor *= 1.1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed_factor = 1
        self.bounce_x()
