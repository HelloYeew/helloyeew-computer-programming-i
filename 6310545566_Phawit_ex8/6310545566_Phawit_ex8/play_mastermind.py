from mastermind import *

new_game = MasterMindBoard()
while (True):
    input_config = input("Make your guess: ")
    MasterMindBoard.guess(input_config)
    MasterMindBoard.display_clue()
    if MasterMindBoard.done():
        break