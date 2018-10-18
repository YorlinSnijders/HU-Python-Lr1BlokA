import time

def toon_aantal_kluizen_vrij():
    print('[Aantal kluizen]')
    f = open('kluizen.txt', 'r')
    lenght = len(f.readlines())
    f.close()

    if lenght >= 12:
        print('Helaas zijn geen kluizen beschikbaar')
    else:
        print('Er zijn %d kluizen beschikbaar' %(12-lenght))

def nieuwe_kluis():
    print('[Nieuwe kluis]')
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    for kluis in kluizen:
        num = int(kluis.split(';')[0])
        if num in kluisnummers:
            kluisnummers.remove(num)

    if len(kluisnummers) >0:
        code = input('Voer een code in: ')
        if len(code) >=4:
            f = open('kluizen.txt', 'a')
            f.write('%d;%s\n' % (kluisnummers[0], code))
            f.close()
            print('Uw kluisnummer is %d en uw code is %s' % (kluisnummers[0], code))
        else:
            print('Uw code is niet lang genoeg')
    else:
        print('Helaas zijn er geen kluizen beschikbaar')
    time.sleep(5)

def kluis_openen():
    print('[Kluis openen]')
    try:
        kluisje = int(input('Geef uw kluisnummer: '))
    except ValueError:
        print('Kluisje moet een nummer zijn')
        time.sleep(5)
        return
    codekluis = input('Code: ')
    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    for kluis in kluizen:
        kluisinfo = kluis.split(';')
        if (int(kluisinfo[0]) == kluisje) and (kluisinfo[1].strip() == codekluis):
            print('De gegevens zijn correct')
            time.sleep(5)
            return
    print('De gegevens zijn incorrect')
    time.sleep(5)

def kluis_teruggeven():
    print('[Kluis teruggeven]')
    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()
    try:
        kluisje = int(input('Kluisnummer: '))
    except ValueError:
        print('Kluisnummer moet een cijfer zijn')
        time.sleep(5)
        return
    code = input('Code: ')

    kluisbestaat = False

    for kluis in kluizen:
        kluisinfo = kluis.split(';')
        if (int(kluisinfo[0]) == kluisje ) and (kluisinfo[1].strip() == code):
            kluisbestaat = True

    if kluisbestaat:
        f = open('kluizen.txt', 'w')
        for kluis in kluizen:
            kluisinfo = kluis.split(';')
            if (int(kluisinfo[0] != kluisje)):
                f.write(kluis)
        f.close()
        print('De kluis is vrijgegeven')
        time.sleep(5)
    else:
        print('Kluis is niet vrijggegeven')
        time.sleep(5)

while  True:
    print('''1: ik wil weten hoeveel kluizen nog vrij zijn\n 2: Ik wil een nieuwe kluis\n 3: Ik wil iets uit mijn kluis halen\n 4: Ik geef mijn kluis terug\n 5: Ik wil stoppen''')
    keuze = 0

    try:
        keuze = int(input('>'))
    except ValueError:
        error()
        continue

    if (keuze <1 or keuze >5):
        error()
        continue
    else:
        if keuze == 1:
            toon_aantal_kluizen_vrij()
        elif keuze == 2:
            nieuwe_kluis()
        elif keuze == 3:
            kluis_openen()
        elif keuze == 4:
            kluis_teruggeven()
        elif keuze == 5:
            break