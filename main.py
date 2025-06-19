from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddle
    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.distance(paddle_left) < 50 or ball.distance(paddle_right) < 50:
            ball.paddle_bounce()

    if ball.xcor() > 380 :
        ball.restart()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.right_point()
screen.exitonclick()