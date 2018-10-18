stations = [
    'Schagen',
    'Heerhugowaard',
    'Alkmaar',
    'Castricum',
    'Zaandam',
    'Amsterdam Sloterdijk',
    'Amsterdam Centraal',
    'Amsterdam Amstel',
    'Utrecht Centraal',
    '’s-Hertogenbosch',
    'Eindhoven',
    'Weert',
    'Roermond',
    'Sittard',
    'Maastricht'
]


def inlezen_beginstation(stations):
    while True:
        beginstation = input('Het beginstation van uw reis is?\n>>>')
        if beginstation in stations:
            return beginstation
        print('Station is niet aanwezig in dit traject')

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Het eindstation van uw reis is?\n>>> ')
        if eindstation in stations:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            elif stations.index(beginstation) == stations.index(eindstation):
                print('Gefeliciteerd je bent al op het station')
            else:
                print('Dit station komt voor het beginstation')
        else:
            print('Deze trein komt niet in %s' % (eindstation))

def omroepen_reis(stations, beginstation, eindstation):
    beginindex = stations.index(beginstation)
    eindindex = stations.index(eindstation)

    print('\nHet beginstation %s is het %de station in het traject' % (beginstation, beginindex +1))
    print('Het eindstation %s is het %de tation in het traject ' % (eindstation, eindindex +1))
    print('De afstand tussen je stations is %d stations' % (eindindex - beginindex))
    print('De prijs voor je reis is €%d,-\n' % ((eindindex - beginindex)*5))

    print('Jij stapt in op station %s' % (beginstation))
    for i in range(beginindex +1, eindindex ):
        print('- %s' % (stations[i]))
    print('Jij stapt uit in: %s' % (eindstation))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)