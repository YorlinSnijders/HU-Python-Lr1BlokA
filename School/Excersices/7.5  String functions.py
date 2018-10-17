def gemiddelde():
    zin = input('Geef mij een willekeurige zin: ').split(' ')

    som = 0

    for woord in zin:
        som += len(woord)
    print('De gemiddelde lengte van een woord is: %.1f' % (som / len(zin)))


gemiddelde()