from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score=0
        with open(r"C:\Users\isha\Desktop\python100Days\TurtleCrossingGame\data.txt") as file:
            self.high_score=int(file.read())
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-200,240)
        self.write(f'Score:{self.score} High-Score:{self.high_score}',align="center",font=("courier",10))
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\isha\Desktop\python100Days\TurtleCrossingGame\data.txt",mode="w") as file:
                 file.write(f"{self.high_score}")
        self.score=0   
        self.update() 
    def add_point(self):
        self.score+=1
        self.clear()
        self.update()