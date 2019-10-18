import csv
from collections import Counter, OrderedDict
from typing import Callable

filePath = 'data/survey_results_public.csv'


def format(n: int, total: int):
    return round(n / total * 100, 2)


def count(callback: Callable[[Counter, OrderedDict], Counter]):
    counter = Counter()

    with open(filePath) as f:
        csv_reader = csv.DictReader(f)

        for line in csv_reader:
            callback(counter, line)

    return counter


def countHobbyists():
    # ? declare function of type
    # def increment: Callable[[Counter, OrderedDict], Counter](c, l):
    def increment(c: Counter, l: OrderedDict):
        c[l['Hobbyist']] += 1

    counter = count(increment)

    total = counter['Yes'] + counter['No']

    yes_pct = format(counter['Yes'], total)
    no_pct = format(counter['No'], total)

    print(yes_pct)
    print(no_pct)


# countHobbyists()

def countUsersByLanguage():
    def increment(c: Counter, l: OrderedDict):
        languages = l['LanguageWorkedWith'].split(';')

        for language in languages:
            c[language] += 1

    counter = count(increment)

    print(counter)


countUsersByLanguage()
