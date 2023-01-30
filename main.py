import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
speed=0.1
screen = Screen()
screen.tracer(0)
carmanager=CarManager()
screen.setup(width=600, height=600)

player=Player()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True

score=Scoreboard()
while game_is_on:

    time.sleep(speed)
    screen.update()
    carmanager.createcar()
    carmanager.move()
    for carr in carmanager.listcars:
        if carr.distance(player) < 20:
            print("Collision occured.")
            game_is_on=False
            score.gameover()

    if player.ycor()>280:
        carmanager.levelup()
        score.clear()
        score.update()
        player.back_home()


screen.exitonclick()
