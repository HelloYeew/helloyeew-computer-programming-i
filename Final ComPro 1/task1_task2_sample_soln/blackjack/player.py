
class Player:
    '''This class describes a player hand in a card game
    '''
    def __init__(self, type, id):
        self.score = 0
        self.id = id
        self.type = type
        self.hand = []
        self.hand_value = 0
    
    def add_hand(self, player_cards):
        self.hand += player_cards
    
    def set_hand_value(self, value):
        self.hand_value = value
    
    def clear_hand(self):
        self.hand = []
        self.hand_value = 0

    def add_score(self, point):
        self.score += point

    def clear_score(self):
        self.score = 0
