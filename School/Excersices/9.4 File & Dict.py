def ticker(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    symbolen = {}

    for line in lines:
        info = line.split(':')
        symbolen[info[0]] = info[1].rstrip()
    return symbolen

symbolen = ticker('ticker.txt')

bedrijfsnaam = input('Enter Company name: ')
print('Ticker symbol: %s\n' % (symbolen[bedrijfsnaam]))

tickie = input('Enter Ticker: ')
bedrijven = symbolen.keys()

for comp in bedrijven:
    symbolen[comp] = symbolen[comp]
    if symbolen[comp] == tickie:
        print(comp)
        break

