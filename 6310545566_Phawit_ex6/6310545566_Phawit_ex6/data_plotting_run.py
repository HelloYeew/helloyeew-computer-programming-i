import data_processing as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = []  # list of countries
temperature = []  # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU += 1
plt.pie([numEU, numNotEU], labels=['EU', 'not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline
data = dp.population_countries_no_coastline_in_EU(dp.countries_data)
country = []
population = []
for i in range(len(data)):
    zip_dict = zip(data[i].keys(), data[i].values())
    zip_dict = list(zip_dict)
    country.append(zip_dict[0][0])
    population.append(zip_dict[0][1])
plt.bar(country, population)
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

# Pie chart showing number of EU cities versus non-EU cities
data = dp.cities_in_EU(dp.cities_data, dp.countries_data)
EU = 0
non_EU = 0
for i in range(len(data)):
    if data[dp.cities_data[i]["city"]] == "yes":
        EU += 1
    else:
        non_EU += 1
plt.pie([EU, non_EU], labels=['EU cities', 'non-EU cities'], autopct='%1.1f%%')
plt.show()

# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)
data = dp.players_data
data_minute = []
data_pass = []
color = []
for i in range(len(data)):
    data_minute.append(int(data[i]["minutes"]))
    data_pass.append(int(data[i]["passes"]))
    if data[i]["position"] == "goalkeeper":
        color.append("red")
    elif data[i]["position"] == "defender":
        color.append("blue")
    elif data[i]["position"] == "midfielder":
        color.append("green")
    elif data[i]["position"] == "forward":
        color.append("dimgray")
plt.scatter(data_minute, data_pass, c=color)
plt.xlabel("Minutes")
plt.ylabel("Passes")
# print(data_minute)
# print(data_pass)
# print(color)
plt.show()

# Bar chart showing average number of passes made by each player postion (defender, midfielder, forward, goalkeeper)
data = dp.average_passes(dp.players_data)
position = ["defender", "midfielder", "forward", "goalkeeper"]
plt.bar(position, data)
plt.xlabel("Position")
plt.ylabel("Passes Average")
plt.show()

# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second', 'third'
data = [dp.class_survival_rate(1, dp.titanic_data), dp.class_survival_rate(2, dp.titanic_data),
        dp.class_survival_rate(3, dp.titanic_data)]
classes = ["First", "Second", "Third"]
plt.bar(classes, data)
plt.xlabel("Class")
plt.ylabel("Survival Rate")
plt.show()

# Pie chart showing the number of male survivors versus female survivors
survivor_male = dp.gender_survival_number("M", dp.titanic_data)
survivor_female = dp.gender_survival_number("F", dp.titanic_data)
plt.pie([survivor_male, survivor_female], labels=['Male', 'Female'], autopct='%1.1f%%')
plt.show()
