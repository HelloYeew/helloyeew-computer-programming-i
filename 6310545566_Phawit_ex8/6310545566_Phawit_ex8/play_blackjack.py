from blackjack import *
from card_deck import *

new_BJ = Blackjack()
new_BJ.start()

while True:
    # player plays
    while new_BJ.player_hand_status!= 'can_stay':
        new_BJ.adjust_player_hand()
        new_BJ.display_player_hand(len(new_BJ.player_hand))

    while new_BJ.player_hand_status == 'can_stay':
        to_stay_or_not = bool(input("More cards? "))
        if to_stay_or_not == False:
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand(len(new_BJ.player_hand))
        else:
            new_BJ.player_hand_status = 'stay'

    # computer plays
    while new_BJ.computer_hand_status != 'can_stay':
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand(len(new_BJ.computer_hand))
    while new_BJ.computer_hand_value < new_BJ.player_hand_value and new_BJ.computer_hand_status == 'can_stay':
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand(len(new_BJ.computer_hand))
        new_BJ.decision()
        if new_BJ.decision() == True:
            play_new_round = input("Play a new round: ")
            if play_new_round == "Yes":
                print()
                continue
            else:
                break
