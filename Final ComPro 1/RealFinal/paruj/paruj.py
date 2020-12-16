import random

class CardDeck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack','Queen', 'King', 'Ace']
        suits = ['\u2663', '\u2666', '\u2665', '\u2660']
        deck = []
        for i in ranks:
            for j in suits:
                card = f"{i} {j}"
                deck.append(card)
        self.card_deck = deck
        self.card_draw_number = 0

    def shuffle_deck(self):
        for i in range(len(self.card_deck)):
            ranged = random.randrange(i,len(self.card_deck))
            card_temp = self.card_deck[ranged]
            self.card_deck[ranged] = self.card_deck[i]
            self.card_deck[i] = card_temp

    def draw_card(self,num):
        draw = []
        for i in range(self.card_draw_number,self.card_draw_number+num):
            draw.append(self.card_deck[i])
        self.card_draw_number += num
        return draw

class Player:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def detect_score(self,card):
        if "Jack" in card:
            score = 11
        elif "Queen" in card:
            score = 12
        elif "King" in card:
            score = 13
        elif "Ace" in card:
            score = 14
        else:
            split_card = card.split(" ")
            score = int(split_card[0])
        return score

    def define_win(self,card1,card2):
        score_card1 = self.detect_score(card1)
        score_card2 = self.detect_score(card2)
        if score_card1 > score_card2:
            return 1
        else:
            return 2

    def edit_score_player1(self,num):
        self.player1_score += num

    def edit_score_player2(self,num):
        self.player2_score += num

    def print_score(self):
        print(f"Player 0 score is: {self.player1_score}")
        print(f"Player 1 score is: {self.player2_score}")


card_deck = CardDeck()
card_deck.shuffle_deck()
draw_card_deck = card_deck.draw_card(10)
card_number_now = 0
player = Player()
# print(draw_card_deck)
for i in range(5):
    print(f"Session {i}")
    print(f"Player 0 hand: {draw_card_deck[card_number_now]}")
    card_player1 = draw_card_deck[card_number_now]
    card_number_now += 1
    print(f"Player 1 hand: {draw_card_deck[card_number_now]}")
    card_player2 = draw_card_deck[card_number_now]
    card_number_now += 1
    if player.define_win(card_player1,card_player2) == 1:
        player.edit_score_player1(1)
        player.edit_score_player2(-1)
    else:
        player.edit_score_player1(-1)
        player.edit_score_player2(1)
    print()
    player.print_score()
    print()
