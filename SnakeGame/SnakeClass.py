from turtle import Turtle,Screen
sposition=[(0,0),(-20,0),(-40,0)]
up=90
down=270
right=0
left=180
class snake:
    def __init__(self) -> None:
        self.all_turtle=[]
        for position in sposition:
           self.add_segment(position)
        self.head=self.all_turtle[0]
        
         
    def add_segment(self,position):
            turtle=Turtle("square")
            turtle.color("green")
            turtle.penup()
            turtle.goto(position)
            self.all_turtle.append(turtle)
            
    def extend(self):
        self.add_segment(self.all_turtle[-1].position())
    def move(self):
       for seg in range(len(self.all_turtle)-1,0,-1):
            x=self.all_turtle[seg-1].xcor()
            y=self.all_turtle[seg-1].ycor()
            self.all_turtle[seg].goto(x,y)
       self.head.forward(20) 
    def reset(self):
        for turtle in self.all_turtle:
            turtle.goto(1000,1000)
        self.all_turtle.clear()
        for position in sposition:
           self.add_segment(position)
        self.head=self.all_turtle[0]
    
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
        
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
        
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
        
        
   