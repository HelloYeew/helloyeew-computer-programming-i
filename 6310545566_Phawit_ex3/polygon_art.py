import turtle
import random

turtle.speed(25)
turtle.setheading(0)


def polygon(x, y, size, n, clr):
    turtle.penup()
    turtle.color(clr)
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(size)
        turtle.left(360 / n)
    turtle.end_fill()
    turtle.penup()


for loop in range(30):
    point_x = random.randint(-325, 325)
    point_y = random.randint(-325, 325)
    shape_size = random.randint(30, 100)
    shape_side = random.randint(3, 8)
    color = "blue"
    polygon(point_x, point_y, shape_size, shape_side, color)
turtle.done()
