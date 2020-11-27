from mastermind import *

new_game = MasterMindBoard()
while True:
    print(new_game.show_number())
    input_guess = input("What is your guess?: ")
    print('Your guess is', input_guess)
    if new_game.check_guess(input_guess) == False:
        print(new_game.display_clue())
        print()
    else:
        print()
        print(new_game.done())
        break

# fix display_clue and test