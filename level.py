from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Level:{self.level}",align='center',font=FONT)
    def update(self):
        self.level+=1
        self.write(f"Level:{self.level}",align='center',font=FONT)
    def gameover(self):
        self.clear()
        self.home()
        self.write("GAME OVER",align='center',font=FONT)
