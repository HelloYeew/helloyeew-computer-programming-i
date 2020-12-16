class Football:
    def __init__(self, short_name="", full_name="", win=0, draw=0, lose=0):
        self.__full_name = full_name
        self.__short_name = short_name
        self.__win = win
        self.__draw = draw
        self.__lose = lose

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, num):
        self.__win = num

    @property
    def draw(self):
        return self.__draw

    @draw.setter
    def draw(self, num):
        self.__draw = num

    @property
    def lose(self):
        return self.__lose

    @lose.setter
    def lose(self, num):
        self.__lose = num

    def __str__(self):
        return f"{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}"


ARS = Football("ARS","Arsenal")
print(ARS)
ARS.win = 1
print(ARS)
ARS.draw = 4
print(ARS)
ARS.lose = 2
print(ARS)
print(ARS.win)
print(ARS.draw)
print(ARS.lose)
