class CardDeck:
    '''This class describes a deck of 52 cards with 4 suits and 13 ranks
    '''
    def __init__(self):
        SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
        'Queen', 'King', 'Ace']
        deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = rank + ' ' + suit
                deck += [card]
        self.card_deck = deck
        self.card_draw_number = 0

    # list of methods
    # must be able to shuffle it
    def shuffle(self):
        import random
        n = len(self.card_deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.card_deck[r]
            self.card_deck[r] = self.card_deck[i]
            self.card_deck[i] = temp

    # must be able to draw n cards from it
    def draw_cards(self,n):
        card_draw = []
        for i in range(self.card_draw_number,self.card_draw_number+n):
            card_draw.append(self.card_deck[i])
        self.card_draw_number += n
        return card_draw

