class Deck:
    """This class represents a deck of 52 cards with 4 suits and 13 ranks"""

    def __init__(self):
        """Generate cards to be put in the deck"""
        deck = []
        SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
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
        return self

    def draw_card(self, count):
        """Draw cards from the deck. Returns a list of drawn cards."""
        drawn_cards = []
        for i in range(count):
            drawn_cards.append(self.card_deck[i])
        return drawn_cards

    def __str__(self):
        """Returns a string representation of this deck class"""
        card_str = ""
        card_str += "| "
        for card in self.card_deck:
            card_str += card + " | "
        return card_str


class BlackJack:
    """This class describes the game of Blackjack itself"""
    def __init__(self):
        deck = Deck()
        self.start()
        self.bj_deck = deck.shuffle()
        self.player_hand = []
        self.computer_hand = []
        self.player_hand_value = ...  # can have multiple values when hand involves Aces
        self.computer_hand_value = ...  # can have multiple values when hand involves Aces
        self.player_hand_status = ...  # [stay or dead or can_stay or must_draw_more]
        self.computer_hand_status = ...  # [stay or dead or can_stay or must_draw_more]

    def start(self):
        """'''This method starts the game by drawing from the card deck (represented by
        self.bj_deck) two cards for player and two cards for computer; then it proceed to update all
        the values and statuses for both hands"""
        self.player_hand = [i for i in self.bj_deck.draw_card(2)]
        self.computer_hand = [i for i in self.bj_deck.draw_card(2)]
        print(self.player_hand)
        print(self.computer_hand)

    def adjust_player_hand(self):
        """This method draws an additional card and reevalute the value and status of the
        player hand"""


    def adjust_computer_hand(self):
        """This method draws an additional card and reevalute the value and status of the
        computer hand"""


    def display_player_hand(self):
        """This method reveals the player hand"""

    def display_computer_hand(self):
        """This method reveals the computer hand"""

    def decision(self):
        """This method makes a decision if the player wins, looses, or ties with the computer"""

# playing BlackJack
new_bj_game = BlackJack()
new_bj_game.start()
new_bj_game.display_computer_hand()
new_bj_game.display_player_hand()

# player plays
while new_bj_game.player_hand_status != 'can_stay':
    new_bj_game.adjust_player_hand()
    new_bj_game.display_computer_hand()

while new_bj_game.player_hand_status == 'can_stay':
    to_stay_or_not = input("stay or not")
    if to_stay_or_not == 'stay':
        new_bj_game.player_hand_status = 'stay'
    else:
        new_bj_game.adjust_player_hand()

# computer plays
while new_bj_game.computer_hand_status != 'can_stay':
    new_bj_game.adjust_computer_hand()
    new_bj_game.display_computer_hand()

while new_bj_game.computer_hand_status == 'can_stay':
    if new_bj_game.display_player_hand() <
# new_BJ = BlackJack()
# new_BJ.start()
# # player plays
# while new_BJ.player_hand_status != 'can_stay':
#     new_BJ.adjust_player_hand()
#     new_BJ.display_player_hand()
# while new_BJ.player_hand_status == 'can_stay':
#     to_stay_or_not = input("stay or not")
#     if not to_stay_or_not:
#         new_BJ.adjust_player_hand()
#         new_BJ.display_player_hand()
#     else:
#         new_BJ.player_hand_status = "stay"
# # computer plays
# while new_BJ.computer_hand_status != 'can_stay':
#     new_BJ.adjust_computer_hand()
#     new_BJ.display_computer_hand()
# while new_BJ.computer_hand_value < new_BJ.player_hand_value and new_BJ.computer_hand_status == 'can_stay':
#     new_BJ.adjust_computer_hand()
#     new_BJ.display_computer_hand()
# new_BJ.decision()
