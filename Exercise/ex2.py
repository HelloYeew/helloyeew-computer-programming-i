# 1. Particles
spin = input("Spin: ")
electric_charge = input("Charge: ")
particle = str()
classes = str()

if spin == "1/2":
    if electric_charge == "-1/3":
        particle = "Strange"
        classes = "Quark"
    elif electric_charge == "2/3":
        particle = "Charm"
        classes = "Quark"
    elif electric_charge == "-1":
        particle = "Electron"
        classes = "Lepton"
    elif electric_charge == "0":
        particle = "Neutrino"
        classes = "Lepton"
else:
    particle = "Photon"
    classes = "Boson"

print(f"{particle} {classes}")

# 2. Calculator
number1 = float(input())
number2 = float(input())
arithmetic = str(input())
if arithmetic == "+":
    answer = number1 + number2
    print(answer)
elif arithmetic == "-":
    answer = number1 - number2
    print(answer)
elif arithmetic == "/":
    if number2 == 0:
        print("Division by 0!")
    else:
        answer = number1 / number2
        print(answer)
elif arithmetic == "*":
    answer = number1 * number2
    print(answer)
elif arithmetic == "mod":
    if number2 == 0:
        print("Division by 0!")
    else:
        answer = number1 % number2
        print(answer)
elif arithmetic == "pow":
    answer = number1 ** number2
    print(answer)
elif arithmetic == "div":
    if number2 == 0:
        print("Division by 0!")
    else:
        answer = number1 // number2
        print(answer)

# 3. Farm
money = int(input("Your money: "))
animal = str()
animal_number = int()
if money >= 6769:
    animal_number = money // 6769
    if animal_number > 1:
        animal = "sheep"
    else:
        animal = "sheep"
    print(f"{animal_number} {animal}")
elif money >= 3848:
    animal_number = money // 3848
    if animal_number > 1:
        animal = "cows"
    else:
        animal = "cow"
    print(f"{animal_number} {animal}")
elif money >= 1296:
    animal_number = money // 1296
    if animal_number > 1:
        animal = "pigs"
    else:
        animal = "pig"
    print(f"{animal_number} {animal}")
elif money >= 678:
    animal_number = money // 678
    if animal_number > 1:
        animal = "goats"
    else:
        animal = "goat"
    print(f"{animal_number} {animal}")
elif money >= 23:
    animal_number = money // 23
    if animal_number > 1:
        animal = "chickens"
    else:
        animal = "chicken"
    print(f"{animal_number} {animal}")
else:
    print("None")

# 4. Day
timezone = int(input("Offset: "))
londontime = 10.5
actualtime = londontime + timezone
if actualtime < 0:
    print("Monday")
elif actualtime > 24:
    print("Wednesday")
else:
    print("Tuesday")


# 5. Write a Python function is_even that takes as input the parameter number (an integer) and
# returns True if number is even and False if number is odd.
# Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.
def is_even(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"


print(is_even(3))
print(is_even(6))
print(is_even(79))


# 6. Write a Python function is_leap_year that take as input the parameter year and
# returns True if year (an integer) is a leap year according to the Gregorian calendar
# and False otherwise. The Wikipedia entry for leap years contains a simple algorithmic rule
# for determining whether a year is a leap year. Your main task will be to translate this rule
# into Python.
# "Every year that is exactly divisible by four is a leap year, except for years that are exactly
# divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
# For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and
# 2000 are."

def is_leap_year(year):
    if year % 4 != 0:
        return "False"
    elif year % 100 != 0:
        return "True"
    elif year % 400 != 0:
        return "False"
    else:
        return "True"


print(is_leap_year(1600))
print(is_leap_year(2020))
print(is_leap_year(2057))


# 7. Write a Python function interval_intersect that takes parameters a, b, c, and d and
# returns True if the intervals [a,b] and [c,d] intersect andFalse otherwise. While this test
# may seem tricky, the solution is actually very simple and consists of one line of Python
# code. (You may assume that a≤b and c≤d.)

def interval_intersect(a, b, c, d):
    if a > d or b < c:
        return "False"
    else:
        return "True"


print(interval_intersect(1, 2, 6, 7))
print(interval_intersect(1, 5, 2, 4))
print(interval_intersect(4, 7, 6, 9))


# 8. Write a Python function print_digits that takes an integer number in the
# range [0,100) and prints the message "The tens digit is % and the ones digits is
# %" where the percents should be replaced with the appropriate values. The function should
# include an error check for the case when number is negative or greater than or equal
# to 100. In those cases, the function should instead print "Error: Input is not a two-digit
# number.”.

def print_digits():
    number = int(input("number: "))
    if number >= 100:
        print("Error: Input is not a two-digit number")
    else:
        tens = number // 10
        ones = number - (tens * 10)
        print(f"The tens digit is {tens} and the ones digits is {ones}")

print_digits()

# 9. Given numbers a, b, and c, the quadratic equation ax2+bx+c=0 can have zero, one or
# two real solutions (i.e; values for x that satisfy the equation). The quadratic formula
# x=(-b±√(b2−4ac))/2a
# can be used to compute these solutions. The expression b2−4ac is
# the discriminant associated with the equation. If the discriminant is positive, the equation
# has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the
# discriminant is negative, the equation has no solutions.
# Write a Python function smaller_root that takes an input the numbers a, b and c and
# returns the smaller solution to this equation if one exists. If the equation has no real
# solution, print the message "Error: No real solutions" and simply return. Note that, in
# this case, the function will actually return the special Python value None.

def smaller_root():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Error: No real solutions")
    else:
        answer1 = (-b + (d ** 0.5)) / (2 * a)
        answer2 = (-b - (d ** 0.5)) / (2 * a)
        if answer1 > answer2:
            return answer2
        else:
            return answer1

print(smaller_root())

# 10.Write a Python function there_is_odd that takes 3 integers x, y, and z and prints the
# message "There is an odd number whose value is % " where the percents should be
# replaced with the appropriate values when there is an odd value among the three integers.
# The function prints "There is no odd number" when there is no odd integer among the
# three input integers.

def there_is_odd():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        print("There is no odd number")
    elif x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
        print(f"There is an odd number whose value is {z}")
    elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
        print(f"There is an odd number whose value is {y}")
    elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
        print(f"There is an odd number whose value is {x}")
    elif x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
        print(f"There is an odd number whose value is {y}")
    elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
        print(f"There is an odd number whose value is {x}")
    elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
        print(f"There is an odd number whose value is {y}")
    elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
        print(f"There is an odd number whose value is {z}")

there_is_odd()

# 11. Write a Python function list_all_odds that takes 4 integers w, x, y, and z and prints
# the message “This value is odd % " where the percents should be replaced with the
# appropriate values when an odd value is found among the four integers. The number of
# times this message gets printed out equals the number of odd values that exist among the
# four input integers. The function prints "There is no odd number" when there is no odd
# integer among the four input integers.

def list_all_odds():
    w = int(input("w: "))
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    if w % 2 != 0:
        print(f"This value is odd {w}")
    if x % 2 != 0:
        print(f"This value is odd {x}")
    if y % 2 != 0:
        print(f"This value is odd {y}")
    if z % 2 != 0:
        print(f"This value is odd {z}")
    if w % 2 == 0 and x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        print("There is no odd number")

list_all_odds()

# 12.Write a Python function max_of_three that takes 3 integers x, y, and z and prints the
# message “The max value is % " where the percents should be replaced with the
# maximum value among the three input integers.

def max_of_three():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    if x > y and x > z:
        print(f"The max value is {x}")
    elif y > x and y > z:
        print(f"The max value is {y}")
    elif z > x and z > y:
        print(f"The max value is {z}")

max_of_three()