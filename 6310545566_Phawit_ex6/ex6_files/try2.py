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

titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)

def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name, same age, same place of embarkment, and age is under 18; each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    twins = list()
    already_checked = list()
    for person in titanic_data:
        for person_2 in titanic_data:
            if person["age"] != "" and person_2["age"] != "":
                if person["first"] != person_2["first"] and person["last"] == person_2["last"] and float(person["age"]) < 18 and float(person_2["age"]) < 18 and person["age"] == person_2["age"] and person_2["first"] not in already_checked:
                    twins.append((f"{person['last']} {person['first']}", f"{person_2['last']} {person_2['first']}"))
                    already_checked.append(person["first"])
    return twins

print(twin_list(titanic_data))