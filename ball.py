from random import randint
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.ball_speed = 0.1
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setheading(randint(-45, 45))

    def bounce_y(self):
        self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())
        self.ball_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        self.setheading(self.heading() + randint(-10, 10))
        self.ball_speed = 0.1
