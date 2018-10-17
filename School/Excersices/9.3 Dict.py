studenten = {
    'Freek': 6.8,
    'John': 6.4,
    'Rob': 8.4,
    'Mark': 9.3,
    'Hans': 9.9,
    'Bob' : 8.5,
    'Fleur': 9.6,
    'Hidde': 6.7,
}

for naam, cijfer in studenten.items():
    if cijfer >= 9.0:
        print('%s: %.1f' % (naam, cijfer) )