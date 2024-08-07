from turtle import Turtle
import random
colors=["red","green","blue","yellow","pink","brown","black","orange","purple"]

class Cars(Turtle):
    def __init__(self,colors):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=0.5)
        self.color(colors)
        self.penup()
        
        random_y=random.randint(-200,220)
        self.goto(300,random_y)
        self.speed_move=5
        self.setheading(180)
        
    def car_move(self):
        self.forward(self.speed_move)
        if self.xcor()<=-300 or self.xcor()>=300:
            self.hideturtle()
            
    def speed_up(self):
            self.speed_move+=1