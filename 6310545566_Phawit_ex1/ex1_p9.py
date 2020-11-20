import turtle

# 4 hexagon

# up
turtle.color("blue")
turtle.pensize(8)
turtle.pendown()
turtle.circle(80, 360, 6)

# left
turtle.left(90)
turtle.color("red")
turtle.circle(80, 360, 6)

# bottom
turtle.left(90)
turtle.color("yellow")
turtle.circle(80, 360, 6)

# right
turtle.left(90)
turtle.color("green")
turtle.circle(80, 360, 6)

# ---------------------------------
# flag
turtle.speed(6)

# red plus
turtle.penup()
turtle.goto(-400,-40)
turtle.setheading(90)
turtle.color("red")
turtle.fillcolor("red")
turtle.pendown()
turtle.begin_fill()
turtle.forward(80)
turtle.right(90)
turtle.forward(360)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(360)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(360)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(180)
turtle.end_fill()
turtle.penup()

# left up triangle down
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(-400, 60)
turtle.goto(-400, 200)
turtle.goto(-200, 60)
turtle.goto(-400, 60)
turtle.end_fill()

# left up triangle up
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(-60, 240)
turtle.goto(-60, 65)
turtle.goto(-295, 240)
turtle.goto(-60, 240)
turtle.end_fill()

# red rectangle left up
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(-400, 240)
turtle.goto(-140, 60)
turtle.goto(-180, 60)
turtle.goto(-400, 210)
turtle.goto(-400, 240)
turtle.end_fill()

# right up triangle down
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(400, 60)
turtle.goto(400, 200)
turtle.goto(200, 60)
turtle.goto(400, 60)
turtle.end_fill()

# right up triangle up
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(60, 240)
turtle.goto(60, 80)
turtle.goto(330, 240)
turtle.goto(60, 240)
turtle.end_fill()

# red rectangle right up
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(400, 240)
turtle.goto(350, 240)
turtle.goto(60, 60)
turtle.goto(110, 60)
turtle.goto(400, 240)
turtle.end_fill()

# right up triangle up
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(400, -60)
turtle.goto(400, -200)
turtle.goto(200, -60)
turtle.goto(400, -60)
turtle.end_fill()

# right down triangle down
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(60, -240)
turtle.goto(60, -65)
turtle.goto(295, -240)
turtle.goto(60, -240)
turtle.end_fill()

# red rectangle right down
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(400, -240)
turtle.goto(140, -60)
turtle.goto(180, -60)
turtle.goto(400, -210)
turtle.goto(400, -240)
turtle.end_fill()

# left down triangle down
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(-400, -60)
turtle.goto(-400, -200)
turtle.goto(-200, -60)
turtle.goto(-400, -60)
turtle.end_fill()

# left down triangle up
turtle.pencolor("dark blue")
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.goto(-60, -240)
turtle.goto(-60, -80)
turtle.goto(-330, -240)
turtle.goto(-60, -240)
turtle.end_fill()

# red rectangle left down
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(-400, -240)
turtle.goto(-350, -240)
turtle.goto(-60, -60)
turtle.goto(-110, -60)
turtle.goto(-400, -240)
turtle.end_fill()

# ---------------------------------
# traffic light sign

# yellow square
turtle.penup()
turtle.goto(0, -200)
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(200, 360, 4)
turtle.end_fill()
turtle.penup()

# black square
turtle.left(90)
turtle.goto(180, 0)
turtle.pendown()
turtle.pendown()
turtle.pencolor("black")
turtle.circle(180, 360, 4)
turtle.penup()

# center black rectangle
turtle.goto(30, -90)
turtle.fillcolor("black")
turtle.setheading(90)
turtle.pendown()
turtle.begin_fill()
turtle.forward(180)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()
turtle.penup()

# green light
turtle.goto(0, -80)
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, 360, 100)
turtle.end_fill()
turtle.penup()

# yellow light
turtle.goto(0, -20)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, 360, 100)
turtle.end_fill()
turtle.penup()

# red light
turtle.goto(0, 40)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, 360, 100)
turtle.end_fill()
turtle.penup()