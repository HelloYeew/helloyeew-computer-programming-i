class CardDeck:
    '''This class describes a deck of 52 cards with 4 suits and 13 ranks
    '''
    def __init__(self):
        SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = rank + ' ' + suit
                deck += [card]
        self.card_deck = deck

    def shuffle(self):
        import random
        n = len(self.card_deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.card_deck[r]
            self.card_deck[r] = self.card_deck[i]
            self.card_deck[i] = temp
    
    def draw_cards(self, n):
        hand = []
        for i in range(n):
            hand.append(self.card_deck.pop())
        return hand