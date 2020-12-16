from player import *
from card_deck import *

class BlackJack:
    '''This class describes the game of BlackJack itself
    '''
    def __init__(self, num_players, stay_value):
        self.bj_deck = []
        player_list = []
        # delear is a special player
        dealer = Player('dealer', 0)
        player_list.append(dealer)
        for i in range(num_players):
            player = Player('player', i+1)
            player_list.append(player)
        self.players = player_list
        self.stay_value = stay_value

    def start_new_round(self):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        for player in self.players:
            player.clear_hand()
        for round in range(2):
            for player in self.players:
                player.add_hand(self.bj_deck.draw_cards(1))

    def display(self, player, full=False):
        display_str = ""
        if player.type == 'player' or full:
            display_hand = player.hand
        else:
            display_hand = player.hand[1:]
        for each_card in display_hand:
            ltemp = each_card.split()
            if ltemp[1] == 'Clubs':
                display_str += ltemp[0] + '\u2663' + ' '
            elif ltemp[1] == 'Diamonds':
                display_str += ltemp[0] + '\u2666' + ' '
            elif ltemp[1] == 'Hearts':
                display_str += ltemp[0] + '\u2665' + ' '
            else:
                assert ltemp[1] == 'Spades', 'Spades expected'
                display_str += ltemp[0] + '\u2660' + ' '
        if player.type == 'dealer':
            print('Computer hand: ' + display_str)
        else:
            print('Player ' + str(player.id) + ' hand: ' + display_str)  

    def calculate_hand_value(self, player):
        val = 0
        num_ace = 0
        for card in player.hand:
            ltemp = card.split()
            if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                val += int(ltemp[0])
            elif ltemp[0] in ['Jack', 'Queen', 'King']:
                val += 10
            else:
                assert ltemp[0] == 'Ace', 'Ace rank expected'
                num_ace += 1
        if num_ace == 0:
            return val
        else:
            if (val + num_ace - 1 + 11) > 21:
                return val + num_ace
            else:
                return val + num_ace - 1 + 11

    def must_draw_more(self, player):
        hand_val = self.calculate_hand_value(player)
        if hand_val < self.stay_value:
            return True
        else:
            return False
    
    def compute_outcome_and_score(self):
        if self.players[0].hand_value > 21:
            for player in self.players[1:]:
                if player.hand_value <= 21:
                    player.add_score(1)
                    self.players[0].add_score(-1)
                    print('Player', player.id, 'wins!')
                else:
                    print('Player', player.id, 'ties!')
        else:
            for player in self.players[1:]:
                if player.hand_value > 21:
                    player.add_score(-1)
                    self.players[0].add_score(1)
                    print('Player', player.id, 'looses!')                    
                elif player.hand_value > self.players[0].hand_value:
                    player.add_score(1)
                    self.players[0].add_score(-1)
                    print('Player', player.id, 'wins!')
                elif player.hand_value == self.players[0].hand_value:
                    print('Player', player.id, 'ties!')
                else:
                    player.add_score(-1)
                    self.players[0].add_score(1)
                    print('Player', player.id, 'looses!')
        print()
        for player in self.players:
            if player.type == 'dealer':
                print("Computer score is", player.score)
            else:
                print("Player", player.id, "score is:", player.score)
