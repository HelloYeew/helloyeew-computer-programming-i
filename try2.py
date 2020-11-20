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

print("diamond(n) result:") # แก้วรรคข้าวหลัง
print("")
for i in range(0, 7):
    diamond(i)
    print("")