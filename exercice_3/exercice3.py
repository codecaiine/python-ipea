print("Saissir la liste d'entier : ")
maListe = []
valeur = input("Veuillez entrer une valeur: ")
while True:
    if valeur:
        try:
            maListe.append(int(valeur))
        except ValueError:
            continue
    else:
        break
print("Vos valeurs sont : ", maListe)
