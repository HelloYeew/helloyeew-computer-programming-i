import turtle
from ball_OO import *


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
# these 3 is change
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

data_to_run = []
for i in range(num_balls):
    data_to_run.append(Ball(canvas_width,canvas_height,ball_radius))

while (True):
    turtle.clear()
    for i in range(len(data_to_run)):
        data_to_run[i].draw()
        data_to_run[i].move()
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
