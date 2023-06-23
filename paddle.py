from turtle import Turtle

SIZE = 20


class Paddle(Turtle):

    def __init__(self, x, y=0, height=5, width=1):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=height, stretch_len=width)
        self.penup()
        self.goto(x=x, y=y)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + SIZE)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - SIZE)
