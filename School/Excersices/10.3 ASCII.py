def code(invoerstring):
    return ' '.join([chr(ord(c) +3) for c in invoerstring])

print(code('RutteAlkmaarDen Helder'))