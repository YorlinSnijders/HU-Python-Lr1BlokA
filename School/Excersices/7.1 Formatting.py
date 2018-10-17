
def convert (celcius):
    return (celcius * 1.8)+32

def table():
    print('{:2}{:8}{}' .format('', 'F', 'C'))
    for temp in range(-30, 50, 10):
        print('{:5.1f}{:8.1f}'.format(convert(temp), temp))

table()