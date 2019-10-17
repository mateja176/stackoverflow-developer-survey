import csv
from collections import Counter


def format(n: int, total: int):
    return round(n / total * 100, 2)


def count(path: str):
    with open(path) as f:
        csv_reader = csv.DictReader(f)

        counts = Counter()

        for line in csv_reader:
            counts[line['Hobbyist']] += 1

    total = counts['Yes'] + counts['No']

    yes_pct = format(counts['Yes'], total)
    no_pct = format(counts['No'], total)

    print(yes_pct)
    print(no_pct)


count('data/survey_results_public.csv')
