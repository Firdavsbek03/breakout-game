from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        self.form_board()

    def form_board(self):
        self.hideturtle()
        self.speed(100)
        self.penup()
        self.goto((0,-255))
        self.shape("square")
        self.color("darkblue")
        self.turtlesize(stretch_wid=1,stretch_len=8,outline=1)
        self.showturtle()

    def right_key_pressed(self):
        if self.xcor()+40<=295:
            self.forward(40)
        elif 295<=self.xcor()+40<=300:
            self.forward(30)

    def left_key_pressed(self):
        if self.xcor()-40>=-297:
            self.backward(40)
        elif -300<=self.xcor()-20<=-297:
            self.backward(20)