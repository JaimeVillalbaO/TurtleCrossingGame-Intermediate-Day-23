from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 200)
        self.write(f'Level:{self.level}', align= 'left', font= FONT)

    def score_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level:{self.level}', align= 'left', font= FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER BITCH', align='center', font=FONT)
        
    
