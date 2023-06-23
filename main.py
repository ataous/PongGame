from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor(31, 31, 31)
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(360)
left_paddle = Paddle(-360)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
while True:
    ball.forward(20)
    screen.update()
    sleep(ball.ball_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_game()

    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_game()

    if scoreboard.end_game():
        break

screen.exitonclick()
