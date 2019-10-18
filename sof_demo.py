import csv
from collections import Counter

filePath = 'data/survey_results_public.csv'


def format(n: int, total: int):
    return round(n / total * 100, 2)


def count():
    counter = Counter()

    with open(filePath) as f:
        csv_reader = csv.DictReader(f)

        for line in csv_reader:
            counter[line['Hobbyist']] += 1

    return counter


def countHobbyists():
    counter = count()

    total = counter['Yes'] + counter['No']

    yes_pct = format(counter['Yes'], total)
    no_pct = format(counter['No'], total)

    print(yes_pct)
    print(no_pct)


countHobbyists()
