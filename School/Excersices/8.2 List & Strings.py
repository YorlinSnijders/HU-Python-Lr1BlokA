lijst = eval(input('Geef lijst met minimaal 10 strings: '))

nieuwelijst = []

if len(lijst) < 10:
    print('Je lijst is te kort')
else:
    for word in lijst:
        if len(word) == 4:
            nieuwelijst.append(word)
print('Dit is de nieuwe lijst: ' + str(nieuwelijst))