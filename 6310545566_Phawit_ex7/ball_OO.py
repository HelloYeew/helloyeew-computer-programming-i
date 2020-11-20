import turtle
import random

class Ball:
    def __init__(self,canvas_width,canvas_height,ball_radius):
        # self.color = []
        # self.color_list = []
        # self.size = 0
        # self.x = 0
        # self.y = 0
        # self.canvas_width = 0
        # self.canvas_height = 0
        # self.ball_radius = 0
        # self.num_balls = 0
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.xpos = random.randint(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
        self.ypos = random.randint(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
        self.vx = random.randint(1, 0.025 * self.canvas_width)
        self.vy = random.randint(1, 0.025 * self.canvas_width)
        self.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def draw(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color)
        turtle.fillcolor(self.ball_color)
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def move(self):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy



