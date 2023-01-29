from turtle import Turtle
POSITIONS_BORDER=[-368,360,280,-281]
BORDER_LEFT=POSITIONS_BORDER[0]
BORDER_RIGHT=POSITIONS_BORDER[1]
BORDER_TOP=POSITIONS_BORDER[2]
BORDER_BOTTOM=POSITIONS_BORDER[3]
ball_touched_bricks=[]
lives=["♥","♥","♥","♥","♥"]


class Ball(Turtle):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.form_ball()
        self.move_speed=0.1
        self.pace_y=-10
        self.pace_x=10

    def form_ball(self):
        self.penup()
        self.shape("circle")
        self.color("#C27664")

    def move(self):
        self.goto(self.xcor()+self.pace_x,self.ycor()+self.pace_y)

    def check_is_ball_on_paddle(self,paddle):
        if self.distance(paddle)<=15 and 180 < self.heading() < 360:
            self.pace_y*=-1
            self.pace_x*=-1
        elif self.distance(paddle)<80 and -240 >= self.ycor() >= -246:
            self.pace_y*=-1

    def check_brick_hit(self,bricks):
        for brick in bricks:
            if self.distance(brick)<=22 or (self.distance(brick)<=35 and (self.ycor()>=98 or self.ycor()<=124)):
                ball_touched_bricks.append(brick)
                brick.color('#F7F5EB')
                bricks.remove(brick)
                self.pace_y *= -1
                if self.move_speed>0.015:
                    self.move_speed*=.9
                else:
                    self.move_speed*=.999

    def check_border_hit(self):
        if abs(BORDER_LEFT - self.xcor())<10 or abs(self.xcor()-BORDER_RIGHT)<10:
            self.pace_x*=-1
        elif abs(self.ycor()-BORDER_TOP)<10:
            self.pace_y*=-1
        elif self.ycor()<BORDER_BOTTOM:
            self.reset()
            self.form_ball()
            lives.pop()
