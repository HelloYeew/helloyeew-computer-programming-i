# 1. Define a constant 5280 feet in a mile and a variable, miles, with a value of 13
# assigned to it. Then, write an assignment statement that calculates and prints the
# number of feet in 13 miles.


FEET_IN_MILE = 5280
miles = 13
feet = FEET_IN_MILE * miles
print(feet)

# 2. Define variables hours, minutes and seconds; assign values of 7, 21, and 37,
# respectively, to each of those variables. Then, write an assignment statement that
# updates the variable seconds to have a value corresponding to the total number of
# seconds.

hours = 7
minutes = 21
seconds = 37
# calculate the seconds
seconds = hours*3600 + minutes*60 + seconds
print(seconds)

# 3. Define variables width and height; assigns values of 4 and 7 to each of those
# variables, respectively. Then, write a Python statement that calculates and prints the
# length of the perimeter of a rectangle. The perimeter of a rectangle is 2*width +
# 2*height.

width = 4
height = 7
perimeter = 2*width + 2*height
print(perimeter)

# 4. Pre-defines the constant PI and the variable radius corresponding to the radius of a
# circle in inches, write an assignment statement that defines a variable area whose
# value is the area of a circle with radius radius in square inches. Print out the area of a
# circle with radius 8.

PI = 3.14
radius = 8
area = PI * radius ** 2
print(area)

# 5. Pre-defined variables present_value, annual_rate and years, write an assignment
# statement that define a variable future_value whose value is present_value dollars
# invested at annual_rate percent interest, compounded annually for years. The
# future_value is given by the formulas
# present_value*(1+0.01*annual_rate)years.

present_value = 1000
annual_rate = 7
years = 10
future_value = present_value*(1+0.01*annual_rate)*years
print(future_value)

# 6. The distance between two points (x0,y0) (x1,y1) is √((x0−x1)2+(y0−y1)2 ). Predefine
# the variables x0, y0, x1, and y1, write an assignment statement that defines a
# variable distance whose values is the distance between the
# points (x0,y0) and (x1,y1). Calculate and print the distance between the points
# (2,2) and (5,6).

x0 = 2
y0 = 2
x1 = 5
y1 = 6
distance = ((x0-x1)**2+(y0-y1)**2)**0.5
print(distance)

# 7. Heron's formula states the area of a triangle is √(s(s−a)(s−b)
# (s−c)) where a, b and c are the lengths of the sides of the triangle
# and s=0.5(a+b+c) is the semi-perimeter of the triangle. Given the
# variables x0, y0, x1,y1, x2, and y2, write a Python program that computes a
# variable area whose value is the area of the triangle with vertices (x0,y0), (x1,y1)
# and (x2,y2). Calculate and print the area of a triangle whose vertices are (1, 1), (4,
# 1), and (4, 5).

x0 = 1
y0 = 1
x1 = 4
y1 = 1
x2 = 4
y2 = 5
a = x1-x0
b = y2-y1
c = (a**2 + b**2)**0.5
s = (a+b+c)*0.5
area = (s * (s-a) * (s-b) * (s-c))**0.5
print(area)

# 8. Ask a user to enter the desired amount of coffee, in cups. Given this, you can adjust
# the program by calculating how much water, coffee, and milk are necessary to make
# the specified amount of coffee. Note that one cup of coffee made on this coffee
# machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.

cups = int(input("Write how many cups of coffee you will need: "))
water = 200*cups
milk = 50*cups
coffee_beans = 15*cups
print(f"For {cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")
