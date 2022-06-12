print("Saissir la liste d'entier : ")
maListe = []
valeur = input("Veuillez entrer une valeur: ")
while True:
    if valeur:
        maListe.append(int(valeur))
    else:
        break
print(maListe)