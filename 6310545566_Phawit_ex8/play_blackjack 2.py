from blackjack import *
from card_deck import *

new_BJ = Blackjack()

while True:
    new_BJ.start()

    # player plays
    while new_BJ.player_hand_status != 'can_stay':
        new_BJ.player_status()
        new_BJ.adjust_player_hand()
        new_BJ.display_player_hand(len(new_BJ.player_hand))

    if new_BJ.player_hand_status == 'can_stay':
        new_BJ.player_status()
        to_stay_or_not = input("More cards? ")
        if to_stay_or_not == "No" or "no":
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand(len(new_BJ.player_hand))
        else:
            new_BJ.player_hand_status = 'stay'

    # computer plays
    while new_BJ.computer_hand_status != 'can_stay':
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand(len(new_BJ.computer_hand))

    if new_BJ.computer_hand_value < new_BJ.player_hand_value and new_BJ.computer_hand_status == 'can_stay':
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand(len(new_BJ.computer_hand))
        new_BJ.decision()
        if new_BJ.decision() == True:
            play_new_round = input("Play a new round: ")
            if play_new_round == "Yes" or "yes":
                print()
                new_BJ.reset()
                continue
            else:
                break

    # player plays
    while new_BJ.player_hand_status != 'can_stay':
        new_BJ.player_status()
        new_BJ.adjust_player_hand()
        new_BJ.display_player_hand(len(new_BJ.player_hand))

    if new_BJ.player_hand_status == 'can_stay':
        new_BJ.player_status()
        to_stay_or_not = input("More cards? ")
        if to_stay_or_not == "No" or "no":
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand(len(new_BJ.player_hand))
        else:
            new_BJ.player_hand_status = 'stay'