import urllib.request
import csv
import codecs
import sys
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
# team_list = dict()
# j = 0
# team_list_append = {"HomeTeam" : 0, "AwayTeam" : 0, "HomeGoals" : 0, "AwayGoals" : 0}
# for i in data_str:
#     team_list_append.update({"HomeTeam" : i, "AwayTeam" : i, "HomeGoals" : i, "AwayGoals" : i})
#     team_list.update({j : team_list_append})
#     j += 1
team_list = {}
j = 0
for i in data_str:
    team_list.update({j : {"HomeTeam":i[0], "AwayTeam":i[1], "HomeGoals":i[2], "AwayGoals":i[3]}})
    j+=1
print(team_list)