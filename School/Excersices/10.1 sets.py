bruin = {'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('[Overeenkomsten]')
print(bruin.intersection(groen), '\n')

print('[Verschil bruin -> groen]')
print(bruin.difference(groen), '\n')

print('[Verschil groen -> bruin]')
print(groen.difference(bruin), '\n')

print('[Alle stations]')
print(bruin.union(groen))