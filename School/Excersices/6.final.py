def standaardtarief(afstandKM):
    afstand = afstandKM if afstandKM > 0 else 0
    if afstand > 50:
        return 15.0 + (afstand * 0.60)
    else:
        return afstand * 0.80


def ritprijs(leeftijd, weekendrit, afstandKM):
    tarief = standaardtarief(afstandKM)

    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            return (tarief / 100) * (100 - 35)
        else:
            return (tarief / 100) * (100 - 40)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return (tarief / 100) * (100 - 30)

print('Leeftijd lager dan 12 weekend')
print('%.2f' % ritprijs(10, True, -2))
print('%.2f' % ritprijs(10, True, 10))
print('%.2f' % ritprijs(10, True, 60))


