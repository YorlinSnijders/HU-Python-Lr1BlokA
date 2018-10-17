numbs = []

while True:
    getal = int(input('Geef een getal: '))
    if getal == 0:
        break
    numbs.append(getal)
print('Er zijn %d getallen ingevoerd, de som is %d' % (len(numbs),sum(numbs)))