from turtle import Turtle

POSITIONS = [(-338, 200), (-338, 171), (-338, 142), (-338, 113)]
COLORS = ["#850000", "#DC0000", "#FF7B54", '#FFB26B']
bricks = []


def construct_bricks():
    for bricks_row in range(4):
        for _ in range(11):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.speed(0)
            new_turtle.color(COLORS[bricks_row])
            new_turtle.shape("square")
            new_turtle.turtlesize(stretch_wid=1.3, stretch_len=3.2)
            new_turtle.goto(POSITIONS[bricks_row][0] + _ * 66.67, POSITIONS[bricks_row][1])
            bricks.append(new_turtle)
