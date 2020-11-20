class DeckCard:
    '''
    This class describes a deck of 52 cards
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
    def