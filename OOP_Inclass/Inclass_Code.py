class Point2D:
    """Point class represents and operate on x, y coordinate
    """
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def disance_from_origin(self):
        return (self.x*self.x + self.y*self.y)**0.5

    def halfway(self, other):
        halfway_x = (other.x - self.x) / 2
        halfway_y = (other.y - self.y) / 2
        return Point2D(halfway_x,halfway_y)

    def __str__(self):
        return "[{0}, {1}]".format(self.x, self.y)
# p = Point2D()
# print("x coor of p is ", p.x)
# print("y coor of p is ", p.y)
# p.x = 3
# p.x = 4
# print("x coor of p is ", p.x)
# print("y coor of p is ", p.y)
# p = Point2D(10,20)
# print("x coor of p is ", p.x)
# print("y coor of p is ", p.y)
p = Point2D(5, 12)
print(p)
q = Point2D(3, 4)
print(q)
distance_from_p_to_origin = p.disance_from_origin()
p = Point2D()
print(distance_from_p_to_origin)
print()

class Rectangle:
    """
    Rectangle class represents a rectangle object with its size and location
    """
    def __init__(self,point,width,height):
        self.corner = point
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self,dx,dy):
        self.corner.x += dx
        self.corner.y += dy

    def __str__(self):
        return "[{0}, {1}, {2}]".format(self.corner,self.width,self.height)



box1 = Rectangle(5, 10, 5)
print(box1)
box2 = Rectangle(Point2D(20,30),100,200)
print(box2)
print("area of box1 is", box1.area())
print("area of box2 is", box2.area())
box1.grow(30,10)
box1.move(2,3)
print(box1, box1.area())

class Player:
    def __init__(self,name,num_wins,num_plays):
        self.name = name
        self.num_wins = num_wins
        self.num_plays = num_plays

    def