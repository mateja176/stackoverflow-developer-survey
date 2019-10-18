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
    dev_type_info: {
        'total': int,
        'language_counter': Counter
    } = {}

    def increment(c: Counter, l: OrderedDict):
        dev_types = l['DevType'].split(';')

        languages = l['LanguageWorkedWith'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter(),
            })

            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1

    count(increment)

    for dev_type, info in dev_type_info.items():
        print(dev_type)

        for language, value in info['language_counter'].most_common(5):
            total = info['total']
            print(f'\t{language}: {format(value, total)}%')


count_users_by_language()
