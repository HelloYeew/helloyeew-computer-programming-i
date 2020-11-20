import turtle
import random

turtle.speed(25)
turtle.setheading(0)

def pinwheel(num_branch, size, backup):
    turtle.pendown()
    for i in range (num_branch):
        turtle.forward(size)
        turtle.backward(backup)
        turtle.right(360/num_branch)
    turtle.penup()

turtle.penup()
for i in range (10):
    # shuffle zone
    x = random.randint(-325, 325)
    y = random.randint(-325, 325)
    clr_list = random.choice(['red', 'blue', 'gold', 'brown', 'violet', 'pink', 'orange', 'yellow'])
    pensize = random.randint(5, 25)
    side = random.randint(5, 20)
    shapesize = random.randint(25, 150)
    backup = random.randint(25, 150)
    # turtle zone
    turtle.goto(x, y)
    turtle.pencolor(clr_list)
    turtle.pensize(pensize)
    pinwheel(side,shapesize,backup)
turtle.done()