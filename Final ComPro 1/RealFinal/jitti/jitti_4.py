import urllib.request
import csv
import codecs


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
    def result(self,results):
        self.__result = results

    def read(self,url):
        byte = urllib.request.urlopen(url)
        byte_to_str = csv.reader(codecs.iterdecode(byte, 'utf-8'))
        team_list = []
        for i in byte_to_str:
            team_list.append(i)
        team_list.pop(0)
        for j in range(len(team_list)):
            for k in range(len(team_list[j])):
                if team_list[j][k].isnumeric():
                    team_list[j][k] = int(team_list[j][k])
        self.result = team_list


    def __str__(self):
        return self.__result


a = FileReadFromURL()
csv_url = "http://eduserv.ku.ac.th/EPL2020.csv"
a.read(csv_url)
b = a.result

while True:
    menu = input("(s)how summary, (e)nter results, (q)uit: ")
    if menu == "s":
        for i in b:
            for j in range(5):
                print(f"{i[j]},", end="")
            print()
    elif menu == "e":
        result = input("Enter a result: ")
        result_split = result.split(" ",-1)
        # print(result_split)
        if result_split[1] == "won":
            for i in range(len(b)):
                if result_split[0] == b[i][0]:
                    b[i][2] += 1
            for j in range(len(b)):
                if result_split[2] == b[j][0]:
                    b[j][4] += 1
        elif result_split[1] == "losed":
            for i in range(len(b)):
                if result_split[0] == b[i][0]:
                    b[i][4] += 1
            for j in range(len(b)):
                if result_split[2] == b[j][0]:
                    b[j][2] += 1
        elif result_split[1] == "drew":
            for i in range(len(b)):
                if result_split[0] == b[i][0]:
                    b[i][3] += 1
                    continue
            for j in range(len(b)):
                if result_split[2] == b[j][0]:
                    b[j][3] += 1
                    continue
    else:
        print("Bye")
        break
