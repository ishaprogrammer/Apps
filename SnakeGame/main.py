from turtle import Turtle,Screen
from SnakeClass import snake
from foodClass import food
from ScoreboardClass import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)
snake=snake()
foods=food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
score=Scoreboard()   

game=True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(foods)< 15:
        score.add_points()
        snake.extend()
        foods.refresh()
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
       score.reset() 
       snake.reset()
    for turtle in snake.all_turtle:
        if turtle==snake.head:
            pass
        elif snake.head.distance(turtle)<10:
           score.reset()
           snake.reset()
    
screen.exitonclick()