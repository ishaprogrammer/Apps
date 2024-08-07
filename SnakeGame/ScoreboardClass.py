from turtle import Turtle
FONT="courier"
ALIGN="center"
class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        with open(r"C:\Users\isha\Desktop\python100Days\MySnakeGame.py2021\data.txt") as file:
            self.high_score=int(file.read())
        self.update_score()
       
        self.speed("fastest")
    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score:{self.high_score}",align=ALIGN,font=(FONT))
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\isha\Desktop\python100Days\MySnakeGame.py2021\data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGN,font=(FONT))
        
    def add_points(self):
        self.score+=1
        self.update_score()
        
        
    
    