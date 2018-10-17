while True:
    try:
        personen = int(input('Aantal personen: '))
        bedrag = float(4356)
        if personen < 0:
            raise SyntaxError ('Negatieve getallen zijn niet toegestaan')
        print('Prijs per persoon: %.2f'  % (bedrag/personen))
    except TypeError:
        print('Gebruik getallen voor het invoeren van een aantal')
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Onjuiste invoer!')
