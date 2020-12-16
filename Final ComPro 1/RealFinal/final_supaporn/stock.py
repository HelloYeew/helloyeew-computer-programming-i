class Stock:
    def __init__(self,item,amount,price):
        self.item = item
        self.amount = amount
        self.price = price

    def __str__(self):
        return (f"({self.item},{self.amount},{self.price})")