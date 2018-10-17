studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for studentcijfers in studentencijfers:
        antw.append(sum(studentcijfers)/len(studentencijfers))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = 0
    totaalcijfers = 0
    for studentencijfers in studentencijfers:
        for cijfer in studentencijfers:
            antw += cijfer
            totaalcijfers += 1
        return antw/totaalcijfers

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))