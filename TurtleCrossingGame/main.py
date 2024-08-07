from turtle import Screen
from player import Player
from Cars import Cars
from ScoreBoard import ScoreBoard
from Cars import colors
import random
import time

screen=Screen()
screen.screensize(600,600)
screen.tracer(0)
player=Player()
score=ScoreBoard()

all_cars=[]
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(player.move,"Up")
    
    if random.randint(1, 6) == 1:
        new_car = Cars(random.choice(colors))
        all_cars.append(new_car)
        
    for car in all_cars:
        car.car_move()
        if player.distance(car)<20:
           score.reset()
           player.game_over()
           game_on=False
           
    if player.ycor()>230:
        player.restart()
        score.add_point()
        for car in all_cars:
            car.speed_up()

    all_cars = [car for car in all_cars if car.xcor() > -300]
   
screen.exitonclick()