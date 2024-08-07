from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,300)
user_get=screen.textinput("mark your get","which color turtle do you pick?")
all_turtles=[]
colors=["green","pink","purple","blue","red","yellow","gray"]
y_positions=[-100,-70,-40,-10,20,50,80]
for turtle_index in range(0,7):
    new_turtle=Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-225,y_positions[turtle_index])
    all_turtles.append(new_turtle)
is_on=False
if user_get:
    is_on=True
while is_on:
    for turtle in all_turtles:
        if turtle.xcor()>280:
            is_on=False
            winner=turtle.pencolor()
            if winner==user_get:
                 print(f"You've won!, The winner Turtle is {winner}.")
            else:
                 print(f"You've lost!, The winner Turtle is {winner}.")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
