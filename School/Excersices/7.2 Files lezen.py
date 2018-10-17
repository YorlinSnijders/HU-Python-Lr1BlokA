f = open('kaartnummers.txt', 'w')
f.write('''325255, Jan Jansen
334343, Erik Materus
235434, Ali Ahson
645345, Eva Versteeg
534545, Jan de Wilde
345355, Henk de Vries''')
f.close()

fr = open('kaartnummers.txt', 'r')
lines = fr.readlines()
fr.close()

for line in lines:
    items = line.split(', ')

    if items[1][-1] == '\n':
        print('{} heeft kaartnummer {}'.format(items[1][0:-1], items[0]))
    else:
        print('{} heeft kaartnummer: {}'.format(items[1], items[0]))

