class Order:
    def __init__(self,item,amount):
        self.item = item
        self.status = "To process"
        self.amount = amount
        self.cost = 0

    def __str__(self):
        return f"({self.item},{self.amount},{self.cost} Baht,{self.status})"
