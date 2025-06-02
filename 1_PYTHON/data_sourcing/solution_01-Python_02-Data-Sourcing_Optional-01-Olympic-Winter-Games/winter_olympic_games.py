# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    # $CHALLENGIFY_BEGIN
    athletes = {}
    with open(MEDALS_FILEPATH, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Athlete'] not in athletes:
                athletes[row['Athlete']] = 1
            else:
                athletes[row['Athlete']] += 1
    best_athlete = None
    best_athlete_medals_count = 0
    for athlete, medals in athletes.items():
        if medals > best_athlete_medals_count:
            best_athlete = athlete
            best_athlete_medals_count = medals
    return best_athlete
    # $CHALLENGIFY_END


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    # $CHALLENGIFY_BEGIN
    countries = {}
    with open(MEDALS_FILEPATH, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            year = int(row['Year'])
            if min_year <= year <= max_year and row['Medal'] == 'Gold':
                if row['Country'] not in countries:
                    countries[row['Country']] = 1
                else:
                    countries[row['Country']] += 1
    best_country = None
    best_country_medals_count = 0
    for athlete, medals in countries.items():
        if medals > best_country_medals_count:
            best_country = athlete
            best_country_medals_count = medals

    with open(COUNTRIES_FILEPATH, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Code'] == best_country:
                return row['Country']

    return best_country # Could not find country's name in dictionary.csv!
    # $CHALLENGIFY_END

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    # $CHALLENGIFY_BEGIN
    with open(MEDALS_FILEPATH) as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        women = {}
        for row in reader:
            if row['Gender'] == 'Women' and row['Event'] == '5000M':
                if row['Athlete'] in women:
                    women[row['Athlete']] += 1
                else:
                    women[row['Athlete']] = 1
        women = sorted(women.items(), key=lambda k: k[1], reverse=True)
        return list(map(lambda woman: woman[0], women[:3]))
    # $CHALLENGIFY_END
