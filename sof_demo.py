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


def count_hobbyists():
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

def count_users_by_language():
    total = 0

    def increment(c: Counter, l: OrderedDict):
        nonlocal total
        total += 1

        languages = l['LanguageWorkedWith'].split(';')

        c.update(languages)

    counter = count(increment)

    for lang in counter.most_common(5):
        print(lang[0], format(lang[1], total))


count_users_by_language()
