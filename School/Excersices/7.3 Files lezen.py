fr = open('kaartnummers.txt', 'r')
lines = fr.readlines()
fr.close()

feest = []

for line in lines:
    feest.append(line.split(', ') [0])

maxNum = max(feest)

print('Deze file telt %d regels.' % len(lines))
print('Het grootste kaartnummer is: %s en dat staat op regel %d.' % (maxNum, feest.index(maxNum) +1))