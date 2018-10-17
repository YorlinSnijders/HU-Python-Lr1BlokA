getallen = [4, 5, 3, -81]

def kwadraten_som(getallen):
    som = 0
    for g in getallen:
        if g > 0:
            som += g**2
    return som
print(kwadraten_som(getallen))