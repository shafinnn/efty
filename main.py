# This is a sample Python script.
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor('pink')
screen.setup(width=1000, height=500)
screen.title("Welcome to PINGPONG! 🐷 ")
screen.tracer(0)

score = Scoreboard()
bowl = Ball()
right_paddle = Paddle((480, 0))
left_paddle = Paddle((-480, 0))

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 'd')

game_on = True
while game_on:
    time.sleep(bowl.move_speed)
    screen.update()
    bowl.refresh()
    # detect collision with wall
    if bowl.ycor() < -230 or bowl.ycor() > 230:
        bowl.bounce_y()
    # detect collision with wall
    if bowl.distance(right_paddle) < 60 and bowl.xcor() > 460 or bowl.distance(left_paddle) < 60 and bowl.xcor() < -460:
        bowl.bounce_x()
    # collision missed with right paddle
    if bowl.xcor() > 470:
        bowl.reset()
        bowl.bounce_x()
        score.increase_left()
    # collision missed with left paddle
    if bowl.xcor() < -470:
        bowl.reset()
        bowl.bounce_x()
        score.increase_right()
    if score.right_score == 3 or score.left_score == 3:
        score.game_over()
        game_on = False


screen.exitonclick()
