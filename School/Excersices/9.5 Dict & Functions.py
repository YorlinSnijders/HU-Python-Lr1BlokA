def namen():
    names = {}
    while True:
        naam_in = input('Volgende naam: ')
        if len(naam_in) == 0:
            for naam, count in names.items():
                if count == 1:
                    print('Er is %d student met de naam %s' % (count, naam))
                elif count > 1:
                    print('Er zijn %d studenten met de naam %s' % (count, naam))
            break
        else:
            names_exist = names.keys()
            if naam_in in names_exist:
                names[naam_in] += 1
            else:
                names[naam_in]= 1

namen()
