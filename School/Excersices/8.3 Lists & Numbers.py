invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

getallen = [int(i) for i in invoer.split ('-')]
getallen.sort()

print('Gesorteerde lijst van ints: ' + str(getallen))
print('Grootste getal: %d en Kleinste getal: %d' % (max(getallen), min(getallen)))
print('Aantal getallen: %d en Som van de getallen: %d' % (len(getallen), sum(getallen)))
gemiddelde = sum(getallen) / len(getallen)
print('Gemiddelde: ' + str(gemiddelde))