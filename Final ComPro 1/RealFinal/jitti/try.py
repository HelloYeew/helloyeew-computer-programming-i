import urllib.request
import csv
import codecs

url = "http://eduserv.ku.ac.th/EPL2020.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
print(team_list)