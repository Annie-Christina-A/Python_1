from turtle import Turtle
import random
x=Turtle()
colors=["red","blue","pink","gray","aquamarine","burlywood","cyan","green"]
for i in range(3,9):
    angle=360/i
    x.pencolor(random.choice(colors))
    for _ in range(i):
        x.forward(100)
        x.right(angle)
x.screen.mainloop()
