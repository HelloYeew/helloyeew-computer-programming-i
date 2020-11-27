class MasterMindBoard:
    def __init__(self):
        shuffle = ''
        for i in range(4):
            import random
            shuffle += str(random.randint(1, 6))
        self.shuffle = shuffle
        self.guess = ''
        self.clue = ''
        self.round = 0

    def check_guess(self, input_guess):
        self.guess = str(input_guess)
        if self.guess == self.shuffle:
            return True
        else:
            self.round += 1
            return False

    def display_clue(self):
        answer_list = []
        guess_list = []
        for i in range(4):
            answer_list = [int(i) for i in self.shuffle]
        for i in range(4):
            guess_list = [int(i) for i in self.guess]
        clue = ''
        for i in range(4):
            if guess_list[i] in answer_list:
                if guess_list[i] == answer_list[i]:
                    clue += "*"
                else:
                    clue += "o"
        return clue


    def done(self):
        if self.round <= 1:
            return f"You solve it after {self.round} round."
        else:
            return f"You solve it after {self.round} rounds."

    # use for see result
    def show_number(self):
        return f"Result = {self.shuffle}"
