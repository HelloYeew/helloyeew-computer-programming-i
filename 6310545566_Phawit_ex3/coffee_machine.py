# function zone
def summary():
    global water, milk, coffee_beans, disposable_cups, money
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def ask_action():
    print("Write action (buy, fill, take):")
    answer = str(input())
    return answer


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - espresso, 3 - cappuccino:")
    buy_coffee = int(input())
    if buy_coffee == 1:
        water -= 250
        coffee_beans -= 16
        money += 4
        disposable_cups -= 1
    elif buy_coffee == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        disposable_cups -= 1
    elif buy_coffee == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        disposable_cups -= 1


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

summary()

print()

action = ask_action()

if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()

print()

summary()
