class MasterMindBoard:
    def __init__(self):
        str = ''
        for i in range(4):
            import random
            str += random.randint(1,6)
        self.solution = str
        self.num_guesses = 0
        self.guess = ''
        self.clue = ''

    def guess(self,input_config):
        pass

    def display_clue(self):
        pass

    def done(self):
        pass

new_game = MasterMindBoard()
while (True):
    input_config = input("Make your guess: ")
    MasterMindBoard.guess(input_config)
    MasterMindBoard.display_clue()
    if MasterMindBoard.done():
        break