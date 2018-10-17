#winter = (12, 1, 2)
#lente = (3, 4, 5)
#zomer = (6, 7, 8)
#herfst = {9, 10, 11)



def seizoen(maand):
    if maand <1 or maand > 12:
        print ('Geen geldige maand')
    else:
        if  maand <= 2 or maand == 12:
            return ('Het is winter')
        elif maand > 2 and maand < 6:
            return ('Het is lente')
        elif maand > 6 and maand < 9:
            return('Het is zomer')
        else:
            return('Het is herfst')

for i in range (1, 13):
    print('%d, %s' % (i,seizoen(i)))
