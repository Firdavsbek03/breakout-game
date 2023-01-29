import time
from turtle import Screen, getcanvas
from ball import Ball
from paddle import Paddle
from game_bricks import construct_bricks,bricks
from score import ScoreBoard


def clicked(a, b):
    print("Turtle Screen:", a, b)


def motion(event):
    x, y = event.x, event.y
    if x < 377:
        temp = -(377 - x)
    elif x > 377:
        temp = x - 377
    else:
        temp = 0
    if temp - 80 < -377:
        temp = -292
    elif temp + 80 > 377:
        temp = 288
    paddle.goto(temp, y=paddle.ycor())


# Setting up Screen
screen = Screen()
screen.bgcolor("#F7F5EB")
screen.setup(width=750, height=580)
screen.tracer(0)

# Creating paddle object

paddle = Paddle()
score_board=ScoreBoard()

construct_bricks()

# creating a ball instance
ball = Ball()

# Adding listener to key strokes
screen.listen()
screen.onkey(paddle.right_key_pressed, "Right")
screen.onkey(paddle.left_key_pressed, "Left")
screen.onclick(clicked)

# controlling through mouse
canvas = getcanvas()
canvas.bind('<Motion>', motion)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    score_board.update_score_board()
    ball.move()
    ball.check_border_hit()
    ball.check_is_ball_on_paddle(paddle)
    ball.check_brick_hit(bricks)
    if score_board.is_game_over():
        game_is_on=False
        canvas.config(bg="#EFA3C8")
    if score_board.is_winner_found():
        game_is_on=False
        canvas.config(bg="#CFFDE1")

screen.mainloop()
