from turtle import Turtle
from ball import ball_touched_bricks,lives


class ScoreBoard(Turtle):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.score=0
        self.write_score()

    def update_score_board(self):
        self.score=len(ball_touched_bricks)
        self.write_score()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-370.0 ,255.0)
        self.color("#2192FF")
        self.write(f"Score: {self.score}",font=("Arial",18,'bold'))
        self.goto(270,255)
        self.color("#CD0404")
        self.write("".join(lives),font=("Arial",24,'bold'),)

    def is_game_over(self):
        if len(lives)==0:
            self.write_message("The Game Over!!!")
            return True

    def is_winner_found(self):
        if len(ball_touched_bricks)==44:
            self.color("#00337C")
            self.write_message("You are the Winner!!!")
            return True

    def write_message(self,message):
        self.goto(-200,0)
        self.write(message,font=("Arial",36,'bold'))
