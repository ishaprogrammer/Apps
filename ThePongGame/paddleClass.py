from turtle import Turtle
class Paddle(Turtle):
     def __init__(self,position):
          super().__init__()
          self.shape("square")
          self.penup()
          self.color("white")
          self.shapesize(3,1)
          self.goto(position)
     def go_up(self):
        y=self.ycor() + 20
        self.goto(self.xcor(),y)
    
     def go_down(self):
        y=self.ycor() - 20
        self.goto(self.xcor(),y)
     
            