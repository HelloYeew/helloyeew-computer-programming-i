import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = []
        for r in cities_data:
            if r['country'] == country:
                t.append(float(r['temperature']))
        d[country] = sum(t) / len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in
    the following format: (the country whose minimum and maximum city temperatures
    differ the most, min temperature, max temperature, max temperature - min temperature)
    """
    country = []
    for i in range(len(cities_data)):
        if cities_data[i]['country'] not in country:
            country.append(cities_data[i]['country'])
    city = []
    for i in range(len(country)):
        append_city = []
        for k in range(len(cities_data)):
            if cities_data[k]['country'] == country[i]:
                append_city.append(cities_data[k]['city'])
        city.append(append_city)
    for i in range(len(city)):
        for j in range(len(city[i])):
            for k in range(len(cities_data)):
                if cities_data[k]['city'] == city[i][j]:
                    city[i][j] = float(cities_data[k]['temperature'])
    city_temp_diff = []
    for i in range(len(city)):
        city[i] = [max(city[i]), min(city[i])]
        city_temp_diff.append(max(city[i]) - min(city[i]))
    city_temp_diff_sorted = sorted(city_temp_diff)
    answer_diff_index = 0
    for i in range(len(city_temp_diff)):
        if city_temp_diff[i] == max(city_temp_diff_sorted):
            answer_diff = city_temp_diff[i]
            answer_diff_index = city_temp_diff.index(answer_diff)
    answer_country = country[answer_diff_index]
    answer_min_city = min(city[answer_diff_index])
    answer_max_city = max(city[answer_diff_index])
    answer = [answer_country, answer_min_city, answer_max_city, answer_diff]
    return answer


def northern_sounthern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together
    with their associated countries in the following format:
    [(northernmost city, its country), (southernmost city, its country)]
    """
    city = []
    country = []
    latitude_city = []
    for i in range(len(cities_data)):
        city.append(cities_data[i]["city"])
        country.append(cities_data[i]["country"])
        latitude_city.append(float(cities_data[i]["latitude"]))
    northern_most_city = city[latitude_city.index(max(latitude_city))]
    northern_most_country = country[latitude_city.index(max(latitude_city))]
    southern_most_city = city[latitude_city.index(min(latitude_city))]
    southern_most_country = country[latitude_city.index(min(latitude_city))]
    return tuple([(northern_most_city, northern_most_country), (southern_most_city, southern_most_country)])


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline;
    the value associated with each key is the population of that country
    """
    answer_dict = []
    for i in range(len(countries_data)):
        if countries_data[i]["EU"] == "yes" and countries_data[i]["coastline"] == "no":
            answer_dict.append({countries_data[i]["country"]: float(countries_data[i]["population"])})
    return answer_dict


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership",
    e.g., "Graz":"yes" or 'Aalborg':'no';
    the size of the dictionary must equal the number of cities represented in cities_data
    """
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    # for city in cities_data:
    #    for country in countries_data:
    city = []
    country = []
    eu = []
    for i in range(len(cities_data)):
        city.append(cities_data[i]["city"])
        country.append(cities_data[i]["country"])
    for i in range(len(country)):
        for k in range(len(countries_data)):
            if country[i] == countries_data[k]["country"]:
                eu.append(countries_data[k]["EU"])
    answer_dict = {}
    for i in range(len(city)):
        answer_dict.update({city[i]: eu[i]})
    return answer_dict


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries,
    the average temperature of all the cities not in EU countries)
    """
    city_eu = []
    city_eu_temp = []
    city_not_eu = []
    city_not_eu_temp = []
    for i in range(len(cities_data)):
        if cities_in_EU(cities_data, countries_data)[cities_data[i]["city"]] == "yes":
            city_eu.append(cities_data[i]["city"])
        else:
            city_not_eu.append(cities_data[i]["city"])
    for i in range(len(city_eu)):
        for k in range(len(countries_data)):
            if city_eu[i] == cities_data[k]["city"]:
                city_eu_temp.append(float(cities_data[k]["temperature"]))
    for i in range(len(city_not_eu)):
        for k in range(len(countries_data)):
            if city_not_eu[i] == cities_data[k]["city"]:
                city_not_eu_temp.append(float(cities_data[k]["temperature"]))
    return tuple([sum(city_eu_temp) / len(city_eu_temp), sum(city_not_eu_temp) / len(city_not_eu_temp)])


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of
    passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """
    defenders_pass = []
    midfielders_pass = []
    forwards_pass = []
    goalkeepers_pass = []
    for i in range(len(players_data)):
        if players_data[i]["position"] == "defender":
            defenders_pass.append(int(players_data[i]["passes"]))
    for i in range(len(players_data)):
        if players_data[i]["position"] == "midfielder":
            midfielders_pass.append(int(players_data[i]["passes"]))
    for i in range(len(players_data)):
        if players_data[i]["position"] == "forward":
            forwards_pass.append(int(players_data[i]["passes"]))
    for i in range(len(players_data)):
        if players_data[i]["position"] == "goalkeeper":
            goalkeepers_pass.append(int(players_data[i]["passes"]))
    return tuple([sum(defenders_pass) / len(defenders_pass), sum(midfielders_pass) / len(midfielders_pass),
                  sum(forwards_pass) / len(forwards_pass), sum(goalkeepers_pass) / len(goalkeepers_pass)])


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    answer = []
    for i in range(len(teams_data)):
        answer.append(int(teams_data[i]["goalsFor"])/int(teams_data[i]["goalsAgainst"]))
    return teams_data[answer.index(max(answer))]["team"]


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20,
    plays less than 200 minutes and makes more than 100 passes; the format for each tuple is (player's surname,
    team played for, team ranking, minutes played, number of passes)
    """
    team = []
    for i in range(20):
        team.append(teams_data[i]["team"])
    players_data_tuple = []
    for i in range(len(players_data)):
        if (players_data[i]["team"] in team) and (int(players_data[i]["minutes"]) < 200) and (
                int(players_data[i]["passes"]) > 100):
            players_data_tuple.append(
                [players_data[i]["surname"], players_data[i]["team"], team.index(players_data[i]["team"]),
                 players_data[i]["minutes"], players_data[i]["passes"]])
    return tuple(players_data_tuple)

    # Reminder: Convert minutes and passes to integers before comparing to values


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about
    a team and its passes per minute value generated by its players
    """
    team = []
    passes = []
    minutes = []
    for i in range(len(teams_data)):
        team.append(teams_data[i]["team"])
    for i in range(len(team)):
        append_passes = []
        append_minutes = []
        for k in range(len(players_data)):
            if players_data[k]["team"] == team[i]:
                append_passes.append(int(players_data[k]["passes"]))
                append_minutes.append(int(players_data[k]["minutes"]))
        passes.append(append_passes)
        minutes.append(append_minutes)
    answer_tuple = []
    for i in range(len(team)):
        answer_tuple.append([team[i], sum(passes[i]) / sum(minutes[i])])
    return answer_tuple


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked

    Your test code must include at least five test cases with different combinations of place_embarked and age_threshold
    """
    count = 0
    for i in range(len(titanic_data)):
        if titanic_data[i]["age"] == "":
            age = 0
        else:
            age = float(titanic_data[i]["age"])
        if ("Mrs." in titanic_data[i]["first"]) and (place_embarked == titanic_data[i]["embarked"]) and (
                age_threshold < age):
            count += 1
    return count


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    """
    count_total = 0
    count_survive = 0
    for i in range(len(titanic_data)):
        if int(titanic_data[i]["class"]) == passenger_class:
            count_total += 1
    for i in range(len(titanic_data)):
        if (int(titanic_data[i]["class"]) == passenger_class) and (titanic_data[i]["survived"] == "yes"):
            count_survive += 1
    return count_survive / count_total


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    """
    count = 0
    for i in range(len(titanic_data)):
        if (titanic_data[i]["gender"] == passenger_gender) and (titanic_data[i]["survived"] == "yes"):
            count += 1
    return count


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e.,
    same last name, same age, same place of embarkment, and age is under 18; each tuple has the following format:
    (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    answer_tuple = []
    first_name_already_in_list = []
    for i in range(len(titanic_data)):
        for j in range(len(titanic_data)):
            if titanic_data[i]["age"] != "" and titanic_data[j]["age"] != "":
                if float(titanic_data[i]["age"]) < 18 and float(titanic_data[j]["age"]) < 18 and titanic_data[i][
                    "age"] == titanic_data[j]["age"] and titanic_data[i]["first"] != titanic_data[j]["first"] and \
                        titanic_data[i]["last"] == titanic_data[j]["last"]:
                    if titanic_data[j]["first"] not in first_name_already_in_list:
                        answer_tuple.append((f"{titanic_data[i]['last']} {titanic_data[i]['first']}",
                                             f"{titanic_data[j]['last']} {titanic_data[j]['first']}"))
                        first_name_already_in_list.append(titanic_data[i]["first"])
    return answer_tuple
