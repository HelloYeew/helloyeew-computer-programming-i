import math


def mysqrt(a):
    epsilon = 0.0000000000000000000000000000000000000000000000000001
    x = a
    while True:
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            break
        else:
            x = y
    return float(x)

def diff(num):
    return abs(float(mysqrt(num) - math.sqrt(num)))

def test_square_root():
    print("a   mysqrt(a)      math.sqrt(a)   diff")
    print("-   ---------      ------------   ----")
    print(f"1.0 {mysqrt(1):<14.12} {math.sqrt(1):<14.12} {diff(1):<14.12}")
    print(f"2.0 {mysqrt(2):<14.12} {math.sqrt(2):<14.12} {diff(2):<14.12}")
    print(f"3.0 {mysqrt(3):<14.12} {math.sqrt(3):<14.12} {diff(3):<14.12}")
    print(f"4.0 {mysqrt(4):<14.12} {math.sqrt(4):<14.12} {diff(4):<14.12}")
    print(f"5.0 {mysqrt(5):<14.12} {math.sqrt(5):<14.12} {diff(5):<14.12}")
    print(f"6.0 {mysqrt(6):<14.12} {math.sqrt(6):<14.12} {diff(6):<14.12}")
    print(f"7.0 {mysqrt(7):<14.12} {math.sqrt(7):<14.12} {diff(7):<14.12}")
    print(f"8.0 {mysqrt(8):<14.12} {math.sqrt(8):<14.12} {diff(8):<14.12}")
    print(f"9.0 {mysqrt(9):<14.12} {math.sqrt(9):<14.12} {diff(9):<14.12}")

test_square_root()