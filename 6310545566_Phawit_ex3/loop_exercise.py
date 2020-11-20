def fib(n):
    n = n + 1
    a = 1
    b = 1
    if n % 2 != 0:
        print(1, end="  ")
        for i in range(n // 2):
            print(a, end="  ")
            b = b + a
            print(b, end="  ")
            a = a + b
    elif n % 2 == 0 and n != 0:
        print(1, end="  ")
        for i in range((n // 2) - 1):
            print(a, end="  ")
            b = b + a
            print(b, end="  ")
            a = a + b
        print(a, end="  ")


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1


def diamond(n):
    n = n + 1
    loopup = 0
    star = 0
    while loopup < n:
        star += 1
        print_star = "*" * (star * 2)
        front_back = " " * int(((n * 2) - len(print_star)) / 2)
        print(f" {front_back}{print_star}")
        loopup += 1
    while loopup > 0:
        print_star = "*" * (star * 2)
        front_back = " " * int(((n * 2) - len(print_star)) / 2)
        print(f" {front_back}{print_star}")
        loopup -= 1
        star -= 1


print("diamond(n) result:")
print("")
for i in range(0, 7):
    diamond(i)
    print("")


def hailstone(n):
    if n == 1:
        print(n, end="")
    else:
        print(n, end="  ")
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            if n == 1:
                print(n, end="")
            else:
                print(n, end="  ")
        else:
            n = int(n * 3)
            n = int(n + 1)
            if n == 1:
                print(n, end="")
            else:
                print(n, end="  ")


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")


def arith_sum(n):
    runnum = 1
    while runnum <= (n - 1):
        print(runnum, end=" ")
        print("+", end=" ")
        runnum += 1
    sum = int((n / 2) * (n + 1))
    print(f"{runnum} = {sum}", end="")


print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")
