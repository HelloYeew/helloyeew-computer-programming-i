from item import *
from order import *
from stock import *

def print_stock_list(stock_list):
    print("Stock List:")
    for i in stock_list:
        print(i)

def print_item_list(item_list):
    print("Item List:")
    for i in item_list:
        print(i)

def print_order_list(order_list):
    print("Item List:")
    for i in order_list:
        print(i)

def process_order_list(order_list,stock_list):
    # for i in order_list:
    #     for j in stock_list:
    #         if i.item.id == j.item.id:
    #             if j.amount > i.amount:
    for i in range(len(order_list)):
        for j in range(len(stock_list)):
            if order_list[i].item.id == stock_list[j].item.id:
                if stock_list[j].amount > order_list[i].amount:
                    order_list[i].status = "Delivered"
                    stock_list[j].amount -= order_list[i].amount
                    order_list[i].cost = stock_list[j].price*order_list[i].amount
                else:
                    order_list[i].status = "Insufficient"



item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')
print(item1)
print(item2)

print(item1 == item2)
print(item2 == item2)

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)
print(stock3)
print(stock5)

order1 = Order(item1, 10)
print(order1)

# Add your own code to create a list of stocks
stock_list = [stock1,stock2,stock3,stock4,stock5,stock6]

print_stock_list(stock_list)

# Add your own code to create a list of orders
item_list = [item1,item2,item3,item4,item5,item6]

print_item_list(item_list)

order_list = []
print("Read order list from user…")
while True:
    id = int(input("Enter item id (negative to quit): "))
    if id < 0:
        break
    else:
        amount = int(input("Enter amount: "))
        append_order = ...
        for i in item_list:
            if i.id == id:
                append_order = Order(i,amount)
    order_list.append(append_order)

print_order_list(order_list)

process_order_list(order_list, stock_list)

print_order_list(order_list)

print_stock_list(stock_list)
