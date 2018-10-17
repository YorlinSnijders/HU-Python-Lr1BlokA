while True:
    word = input('Geef een string van vier letters: ')
    if len(word) != 4:
        print('%s heeft %d letters' % (word, len(word)))
    else:
        print('Inlezen van correcte string: %s is geslaagd' % (word))
        break