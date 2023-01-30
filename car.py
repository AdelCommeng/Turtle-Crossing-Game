from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_POSITION=-230
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.listcars=[]
        #self.STARTING_POSITION =random.randint(-280,280)
        self.hideturtle()
        self.speeds=5
        # self.shape("square")
        # self.penup()
        # self.goto(300, -230)
        # self.setheading(180)
    def createcar(self):
        randchance=random.randint(1,5) # To minimize many car occurences overlapping each other on the canvas.
        if randchance ==1:

            newcar=Turtle()
            newcar.shape("square")
            newcar.shapesize(1, 2)
            newcar.color(random.choice(COLORS))
            newcar.penup()
            newcar.setheading(180)
            y= random.randint(-250,250)
            newcar.goto(300,y)
            self.listcars.append(newcar)

    def move(self):
        #     x =listcars[xx]
        #     x.forward(STARTING_MOVE_DISTANCE)
        for cars in self.listcars:
                cars.forward(self.speeds)

    def levelup(self):
        self.speeds+=MOVE_INCREMENT
