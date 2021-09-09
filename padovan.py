
liste = [1, 1, 1]

def padovan(nombre):
    for i in range(0, nombre, 1):
        if i < 3:
            print(liste[i])
        else:
            valeur = liste[i-2] + liste[i-3]
            print(valeur)
            liste.append(valeur)

padovan(23)
