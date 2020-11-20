import urllib.request
import csv
import codecs
import sys
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.DictReader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = {}
j = 0
for i in data_str:
    team_list.update({j : {"HomeTeam":i[0], "AwayTeam":i[1], "HomeGoals":i[2], "AwayGoals":i[3]}})
    j+=1
# print(team_list)

def calculate_data(team_list):
    team = []
    for i in range(len(team_list)):
        if team_list[i]["HomeTeam"] not in team:
            team.append(team_list[i]["HomeTeam"])
    for i in range(len(team_list)):
        if team_list[i]["AwayTeam"] not in team:
            team.append(team_list[i]["AwayTeam"])
    team_win = []
    team_lose = []
    team_draw = []
    team_total_match = []
    for i in range(len(team)):
        team_win.append(0)
        team_lose.append(0)
        team_draw.append(0)
        team_total_match.append(0)
    for i in range(len(team_list)):
        if int(team_list[i]["HomeGoals"]) > int(team_list[i]["AwayGoals"]):
            team_win[team.index(team_list[i]["HomeTeam"])] += 1
            team_lose[team.index(team_list[i]["AwayTeam"])] += 1
        elif int(team_list[i]["AwayGoals"]) > int(team_list[i]["HomeGoals"]):
            team_win[team.index(team_list[i]["AwayTeam"])] += 1
            team_lose[team.index(team_list[i]["HomeTeam"])] += 1
        elif int(team_list[i]["HomeGoals"]) == int(team_list[i]["AwayGoals"]):
            team_draw[team.index(team_list[i]["HomeTeam"])] += 1
            team_draw[team.index(team_list[i]["AwayTeam"])] += 1
    for i in range(len(team)):
        team_total_match[i] = team_win[i] + team_lose[i] + team_draw[i]
    return team,team_total_match,team_win,team_draw,team_lose


def level_1(team):
    team,mp,w,d,l = calculate_data(team)
    print(" N |Team              | MP | W | D | L ")
    print("---------------------------------------")
    for i in range(len(team)):
        print(f"{i+1:^3}|{team[i]:<18}|{mp[i]:^4}|{w[i]:^3}|{d[i]:^3}|{l[i]:^3}")


while True:
    command = input("Select Menu (1,Q): ")
    if command == "1":
        level_1(team_list)
    elif command == "Q" or command == "q":
        print("Bye")
        sys.exit()