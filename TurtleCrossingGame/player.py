from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0,-240)
        self.setheading(90)
        
    def move(self):
        self.forward(10)
        
    def game_over(self):
        self.color("black")
        self.goto(0,0)
        self.write('GAME OVER',align="center",font=("courier",10))
        
    def restart(self):
        self.goto(0,-240)
        