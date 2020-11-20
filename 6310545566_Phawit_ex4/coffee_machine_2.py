import sys


# function zone
def summary():
    global water, milk, coffee_beans, disposable_cups, money
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    if money != 0:
        print(f"${money} of money")
    else:
        print(f"{money} of money")


def ask_action():
    print("Write action (buy, fill, take, remaining, exit):")
    answer = str(input())
    return answer


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - espresso, 3 - cappuccino, back - to main menu:")
    buy_coffee = input()
    if buy_coffee == 1:
        if water >= 250 and coffee_beans >= 16 and disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee_beans -= 16
            money += 4
            disposable_cups -= 1
        else:
            if water < 250 and coffee_beans < 16 and disposable_cups < 1:
                print("Sorry, not enough water, coffee beans and disposable cups!")
            elif water < 250 and coffee_beans < 16:
                print("Sorry, not enough water and coffee beans!")
            elif water < 250 and disposable_cups < 1:
                print("Sorry, not enough water and disposable cups!")
            elif coffee_beans < 16 and disposable_cups < 1:
                print("Sorry, not enough coffee beans and disposable cups!")
            elif water < 250:
                print("Sorry, not enough water!")
            elif coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups!")
    elif buy_coffee == 2:
        if water >= 350 and milk >= 75 and coffee_beans >= 20 and disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            disposable_cups -= 1
        else:
            # 1 + 4 + 6 + 4 = 15
            if water < 350 and milk < 75 and coffee_beans < 20 and disposable_cups < 1:
                print("Sorry, not enough water, milk, coffee beans and disposable cups!")
            elif water < 350 and milk < 75 and coffee_beans < 20:
                print("Sorry, not enough water, milk and coffee beans!")
            elif water < 350 and milk < 75 and disposable_cups < 1:
                print("Sorry, not enough water, milk and disposable cups!")
            elif water < 350 and coffee_beans < 20 and disposable_cups < 1:
                print("Sorry, not enough water, coffee beans and disposable cups!")
            elif milk < 75 and coffee_beans < 20 and disposable_cups < 1:
                print("Sorry, not enough milk, coffee beans and disposable cups!")
            elif water < 350 and milk < 75:
                print("Sorry, not enough water and milk!")
            elif water < 350 and coffee_beans < 20:
                print("Sorry, not enough water and coffee beans!")
            elif water < 350 and disposable_cups < 1:
                print("Sorry, not enough water and disposable cups!")
            elif milk < 75 and coffee_beans < 20:
                print("Sorry, not enough milk and coffee beans!")
            elif milk < 75 and disposable_cups < 1:
                print("Sorry, not enough milk and disposable cups!")
            elif coffee_beans < 20 and disposable_cups < 1:
                print("Sorry, not enough coffee beans and disposable cups!")
            elif water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups!")
    elif buy_coffee == 3:
        if water >= 200 and milk >= 100 and coffee_beans >= 12 and disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            disposable_cups -= 1
        else:
            if water < 200 and milk < 100 and coffee_beans < 12 and disposable_cups < 1:
                print("Sorry, not enough water, milk, coffee beans and disposable cups!")
            elif water < 200 and milk < 100 and coffee_beans < 12:
                print("Sorry, not enough water, milk and coffee beans!")
            elif water < 200 and milk < 100 and disposable_cups < 1:
                print("Sorry, not enough water, milk and disposable cups!")
            elif water < 200 and coffee_beans < 12 and disposable_cups < 1:
                print("Sorry, not enough water, coffee beans and disposable cups!")
            elif milk < 100 and coffee_beans < 12 and disposable_cups < 1:
                print("Sorry, not enough milk, coffee beans and disposable cups!")
            elif water < 200 and milk < 100:
                print("Sorry, not enough water and milk!")
            elif water < 200 and coffee_beans < 12:
                print("Sorry, not enough water and coffee beans!")
            elif water < 200 and disposable_cups < 1:
                print("Sorry, not enough water and disposable cups!")
            elif milk < 100 and coffee_beans < 12:
                print("Sorry, not enough milk and coffee beans!")
            elif milk < 100 and disposable_cups < 1:
                print("Sorry, not enough milk and disposable cups!")
            elif coffee_beans < 12 and disposable_cups < 1:
                print("Sorry, not enough coffee beans and disposable cups!")
            elif water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups!")
    else:
        pass


def fill():
    global water, milk, coffee_beans, disposable_cups
    print("Write how many ml of water do you want to add:")
    fill_water = int(input())
    print("Write how many ml of milk do you want to add:")
    fill_milk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    fill_coffee = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    fill_cups = int(input())
    water += fill_water
    milk += fill_milk
    coffee_beans += fill_coffee
    disposable_cups += fill_cups


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


# main zone
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

while True:
    action = ask_action()
    print()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        summary()
    elif action == "exit":
        sys.exit()
    else:
        print("No valid action")
    print()
