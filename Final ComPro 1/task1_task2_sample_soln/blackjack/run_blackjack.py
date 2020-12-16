from blackjack import *

# play Blackjack
num_players = int(input('How many players to deal? '))
BJ = BlackJack(num_players, 16)
new_round = 'Yes'
while new_round != 'No':
    BJ.start_new_round()
    for player in BJ.players:
        BJ.display(player)
    for player in BJ.players:
        if player.type == 'player':
            while BJ.must_draw_more(player):
                player.add_hand(BJ.bj_deck.draw_cards(1))
                BJ.display(player)
            while BJ.calculate_hand_value(player) < 21:
                print('More cards for player?', player.id)
                response = input()
                if response != 'Yes':
                    break
                player.add_hand(BJ.bj_deck.draw_cards(1))
                BJ.display(player)
            player.set_hand_value(BJ.calculate_hand_value(player))
        print()
    for player in BJ.players:
        if player.type == 'dealer':
            while BJ.must_draw_more(player):
                player.add_hand(BJ.bj_deck.draw_cards(1))
                BJ.display(player)
            BJ.display(player, True)
            player.set_hand_value(BJ.calculate_hand_value(player))
    BJ.compute_outcome_and_score()
    new_round = input("Next round? ")
    