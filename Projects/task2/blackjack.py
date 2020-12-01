from card_deck import *

class Blackjack:
    '''This class describes the game of Blackjack itself
    '''
    def __init__(self):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        self.player_hand = []
        self.computer_hand = []
        self.card_number = 0
        self.player_hand_value = 0 # can have multiple values when hand involves Aces
        self.computer_hand_value = 0 # can have multiple values when hand involves Aces
        self.player_hand_status = ... # [stay or dead or can_stay or must_draw_more]
        self.computer_hand_status = ... # [stay or dead or can_stay or must_draw_more]

    def start(self):
        '''This method starts the game by drawing from the card deck (represented by
        self.bj_deck) two cards for player and two cards for computer; then it proceed to update all
        the values and statuses for both hands
        '''
        self.player_hand = [i for i in self.bj_deck.draw_cards(2)]
        self.computer_hand = [i for i in self.bj_deck.draw_cards(2)]
        # print(self.player_hand)
        # print(self.computer_hand)
        print("Let's play Blackjack!")
        print(self.display_player_hand(2))
        print(self.display_computer_hand(1))

    def get_value(self,hand):
        lst = []
        for i in hand:
            if i is list:
                i = str(i)
            temp = i.split(" ")
            lst.append(temp[0])
        return lst


    def player_status(self):
        # if (self.player_hand_value-self.computer_hand_value < 5) and self.player_hand_value > 18:
        self.player_hand_value = self.calculate_value(self.player_hand)
        if self.player_hand_value >= 16:
            self.player_hand_status = "can_stay"


    def computer_status(self):
        self.computer_hand_value = self.calculate_value(self.computer_hand)
        if self.computer_hand_value >= 16:
            self.computer_hand_status = "can_stay"

    def adjust_player_hand(self):
        '''This method draws an additional card and reevalute the value and status of the
        player hand
        '''
        self.player_status()
        if self.player_hand_status != "can_stay":
            self.player_hand += self.bj_deck.draw_cards(1)

    def adjust_computer_hand(self):
        '''This method draws an additional card and reevalute the value and status of the
        computer hand
        '''
        self.computer_status()
        if self.computer_hand_status != "can_stay":
            self.computer_hand += self.bj_deck.draw_cards(1)

    def display_player_hand(self,number):
        '''This method reveals the player hand
        '''
        str_player_hand = "Your hand: "
        for i in range(number):
            str_player_hand += str(self.player_hand[i]) + " "
        return str_player_hand

    def display_computer_hand(self,number):
        '''This method reveals the computer hand
        '''
        str_computer_hand = "Computer hand : "
        for i in range(number):
            str_computer_hand += self.computer_hand[i] + " "
        return str_computer_hand

    def decision(self):
        '''This method makes a decision if the player wins, looses, or ties with the
        computer
        '''
        if self.computer_hand_value < self.player_hand_value <= 21:
            print("You win!")
        elif self.player_hand_value < self.computer_hand_value <= 21:
            print("You lose!")
        else:
            print("You tie with the computer!")
        return True

    def calculate_value(self,hand):
        value = 0
        value2 = 0
        for i in self.get_value(hand):
            if i.isnumeric():
                value += int(i)
            else:
                if i == "Ace":
                    value += 1
                    value2 += 11
                else:
                    value += 10
        if value2 < value <= 21:
            return value
        else:
            return value2

    def reset(self):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        self.player_hand = []
        self.computer_hand = []
        self.card_number = 0
        self.player_hand_value = 0 # can have multiple values when hand involves Aces
        self.computer_hand_value = 0 # can have multiple values when hand involves Aces
        self.player_hand_status = ... # [stay or dead or can_stay or must_draw_more]
        self.computer_hand_status = ...

