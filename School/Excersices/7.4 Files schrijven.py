import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a %d %b %Y, %H:%M:%S')

names = ['Miranda', 'Piet', 'Sacha', 'Karel', 'Kemal']
f = open('hardlopers.txt', 'a')

for name in names:
    f.write('{}, {}\n'.format(s, name))
f.close()

f = open('hardlopers.txt', 'r')

for line in f.readlines():
    print(line)
f.close()