from blackjack import *
from card_deck import *

new_BJ = Blackjack()

while True:
    new_BJ.start()
    current_player = 0
    # player plays
    while current_player < new_BJ.player_number:
        print(new_BJ.display_specific_player_hand(current_player))
        more_card = input("More cards?")
        if more_card == "No" or "no":
            current_player += 1
            print()
        else:
            new_BJ.adjust_player_hand(current_player)
            print(new_BJ.display_specific_player_hand(current_player))
    print(new_BJ.display_player_hand())
    print()
    print(new_BJ.player_result())
    print()
    print(new_BJ.print_player_score())
    print()
    continue_or_not = input("Next round?" )
    if continue_or_not == "Yes" or "yes":
        continue
    else:
        print("Bye! Have a good dream!")
        break


