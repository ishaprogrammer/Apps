from turtle import Turtle,Screen
from paddleClass import Paddle
from ballClass import Ball
from ScoreboardClass import Scoreboard
import time
screen=Screen()
screen.screensize(300,400)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle=Paddle((290,0))
l_paddle=Paddle((-290,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

stop=True
while stop:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>250 or ball.ycor()<-250:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>200 or ball.distance(l_paddle)<50 and ball.xcor()<-200:
        ball.bounce_x()
    if ball.xcor()>280:
        ball.reset()
        score.add_r()
    
    if ball.xcor()<-280:
        ball.reset()
        score.add_l()
    
screen.exitonclick()