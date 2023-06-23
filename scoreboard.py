from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.update()

    def update(self):
        self.write(f"{self.left_score}  {self.right_score}", align=ALIGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.clear()
        self.update()

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update()

    def end_game(self,):
        if self.left_score == 10:
            self.goto(x=0, y=0)
            self.write(arg="Left Player Win.", align=ALIGN, font=FONT)
            return True
        if self.right_score == 10:
            self.goto(x=0, y=0)
            self.write(arg="Right Player Win.", align=ALIGN, font=FONT)
            return True
        return False
