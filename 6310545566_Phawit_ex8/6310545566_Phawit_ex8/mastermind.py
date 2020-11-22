class MasterMindBoard:
    def __init__(self):
        shuffle = ''
        for i in range(4):
            import random
            shuffle += str(random.randint(1, 6))
        self.shuffle = shuffle
        self.num_guesses = 0
        self.guess = ''
        self.clue = ''
        self.round = 0

    def guess(self, input_guess):
        self.guess = input_guess
        pass

    def display_clue(self):
        for i in range(4):
            guess_list = [int(i) for i in self.shuffle]

    def done(self):
        pass

    def show_number(self):
        return f"Result = {self.shuffle}"


new_game = MasterMindBoard()
while (True):
    print(new_game.show_number())
    input_guess = input("What is your guess?: ")
    print('Your guess is', input_guess)
    MasterMindBoard.guess(input_guess)
    MasterMindBoard.display_clue()
    if MasterMindBoard.done():
        break
