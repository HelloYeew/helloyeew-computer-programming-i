class Item:
    def __init__(self,id,type,color):
        self.id = id
        self.type = type
        self.color = color

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.id},{self.type},{self.color}"
    