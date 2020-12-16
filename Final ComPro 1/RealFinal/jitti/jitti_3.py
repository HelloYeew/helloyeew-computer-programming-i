import urllib.request
import csv
import codecs

csv_url = "http://eduserv.ku.ac.th/EPL2020.csv"
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
        self.__win += num

    @property
    def draw(self):
        return self.__draw

    @draw.setter
    def draw(self, num):
        self.__draw += num

    @property
    def lose(self):
        return self.__lose

    @lose.setter
    def lose(self, num):
        self.__lose += num

    def won(self,team):
        self.win = 1
        team.lose = 1

    def drew(self,team):
        self.draw = 1
        team.draw = 1

    def losed(self,team):
        self.lose = 1
        team.win = 1

    def __str__(self):
        return f"{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}"


class FileReadFromURL:
    def __init__(self):
        self.__filename = ""
        self.__result = ...

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self,result):
        self.__result = result

    def read(self,url):
        byte = urllib.request.urlopen(url)
        byte_to_str = csv.reader(codecs.iterdecode(byte, 'utf-8'))
        team_list = []
        for i in byte_to_str:
            team_list.append(i)
        team_list.pop(0)
        self.result = team_list


    def __str__(self):
        return self.__result


a = FileReadFromURL()
a.read(csv_url)
for i in a.result:
    for j in range(5):
        print(f"{i[j]},",end="")
    print()
