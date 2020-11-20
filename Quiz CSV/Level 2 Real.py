import urllib.request
import csv
import codecs
import sys
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
# print(team_list)

def calculate_data_level_1(team_list):
    team = []
    for i in range(1,len(team_list)):
        if team_list[i][0] not in team:
            team.append(team_list[i][0])
    for i in range(1,len(team_list)):
        if team_list[i][1] not in team:
            team.append(team_list[i][1])
    team_win = []
    team_lose = []
    team_draw = []
    team_total_match = []
    for i in range(len(team)):
        team_win.append(0)
        team_lose.append(0)
        team_draw.append(0)
        team_total_match.append(0)
    for i in range(1,len(team_list)):
        if int(team_list[i][2]) > int(team_list[i][3]):
            team_win[team.index(team_list[i][0])] += 1
            team_lose[team.index(team_list[i][1])] += 1
        elif int(team_list[i][3]) > int(team_list[i][2]):
            team_win[team.index(team_list[i][1])] += 1
            team_lose[team.index(team_list[i][0])] += 1
        elif int(team_list[i][2]) == int(team_list[i][3]):
            team_draw[team.index(team_list[i][0])] += 1
            team_draw[team.index(team_list[i][1])] += 1
    for i in range(len(team)):
        team_total_match[i] = team_win[i] + team_lose[i] + team_draw[i]
    return team,team_total_match,team_win,team_draw,team_lose

def calculate_data_level_2(team_list):
    team = []
    for i in range(1,len(team_list)):
        if team_list[i][0] not in team:
            team.append(team_list[i][0])
    for i in range(1,len(team_list)):
        if team_list[i][1] not in team:
            team.append(team_list[i][1])
    team_win = []
    team_lose = []
    team_draw = []
    team_total_match = []
    team_goalfor = []
    team_goalagainst = []
    team_goaldiff = []
    team_point = []
    for i in range(len(team)):
        team_win.append(0)
        team_lose.append(0)
        team_draw.append(0)
        team_total_match.append(0)
        team_goalfor.append(0)
        team_goalagainst.append(0)
        team_goaldiff.append(0)
        team_point.append(0)
    for i in range(1,len(team_list)):
        if int(team_list[i][2]) > int(team_list[i][3]):
            team_win[team.index(team_list[i][0])] += 1
            team_lose[team.index(team_list[i][1])] += 1
        elif int(team_list[i][3]) > int(team_list[i][2]):
            team_win[team.index(team_list[i][1])] += 1
            team_lose[team.index(team_list[i][0])] += 1
        elif int(team_list[i][2]) == int(team_list[i][3]):
            team_draw[team.index(team_list[i][0])] += 1
            team_draw[team.index(team_list[i][1])] += 1
        team_goalfor[team.index(team_list[i][0])] += int(team_list[i][2])
        team_goalfor[team.index(team_list[i][1])] += int(team_list[i][3])
        team_goalagainst[team.index(team_list[i][0])] += int(team_list[i][3])
        team_goalagainst[team.index(team_list[i][1])] += int(team_list[i][2])
    for i in range(len(team)):
        team_total_match[i] = team_win[i] + team_lose[i] + team_draw[i]
        team_goaldiff[i] = team_goalfor[i] - team_goalagainst[i]
        team_point[i] = (team_win[i]*3) + team_draw[i]
    team_point_sort = sorted(team_point,reverse=True)
    team_sort = []
    team_win_sort = []
    team_lose_sort = []
    team_draw_sort = []
    team_total_match_sort = []
    team_goalfor_sort = []
    team_goalagainst_sort = []
    team_goaldiff_sort = []
    for i in range(len(team_point_sort)):
        for k in range(len(team_point)):
            if team_point_sort[i] == team_point[k]:
                if team[k] not in team_sort:
                    team_sort.append(team[k])
                    team_win_sort.append(team_win[k])
                    team_lose_sort.append(team_lose[k])
                    team_draw_sort.append(team_draw[k])
                    team_total_match_sort.append(team_total_match[k])
                    team_goalfor_sort.append(team_goalfor[k])
                    team_goalagainst_sort.append(team_goalagainst[k])
                    team_goaldiff_sort.append(team_goaldiff[k])
    return team_sort,team_total_match_sort,team_win_sort,team_draw_sort,team_lose_sort,team_goalfor_sort,team_goalagainst_sort,team_goaldiff_sort,team_point_sort

def level_1(team):
    team,mp,w,d,l = calculate_data_level_1(team)
    print("| N |Team              | MP | W | D | L |")
    print("-----------------------------------------")
    for i in range(len(team)):
        print(f"|{i+1:^3}|{team[i]:<18}|{mp[i]:^4}|{w[i]:^3}|{d[i]:^3}|{l[i]:^3}|")

def level_2(team):
    team,mp,w,d,l,gf,ga,gd,pts = calculate_data_level_2(team)
    print("| N |Team              | MP | W | D | L | GF | GA | GD | Pts |")
    print("--------------------------------------------------------------")
    for i in range(len(team)):
        print(f"|{i+1:^3}|{team[i]:<18}|{mp[i]:^4}|{w[i]:^3}|{d[i]:^3}|{l[i]:^3}|{gf[i]:^4}|{ga[i]:^4}|{gd[i]:^4}|{pts[i]:^5}|")


while True:
    command = input("Select Menu (1,2,Q): ")
    if command == "1":
        level_1(team_list)
    elif command == "2":
        level_2(team_list)
    elif command == "Q" or command == "q":
        print("Bye")
        sys.exit()