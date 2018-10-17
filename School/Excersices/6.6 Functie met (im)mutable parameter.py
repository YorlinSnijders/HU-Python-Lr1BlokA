lijst = ['a', 'b', 'c']

def wijzig(lijstje):
    del lijst [:]
    lijstje.append ('d')
    lijstje.append ('e')
    lijstje.append ('f')


print(lijst)
wijzig(lijst)
print(lijst)
