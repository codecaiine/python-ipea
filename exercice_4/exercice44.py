print("Bienvenu dans notre programme")
notreListe=[]
while True:
    valeur=input("Veuillez saissir une valeur :")
    if valeur:
        try:
            x=int(valeur)
            notreListe.append(x)
        except ValueError:
            print("Erreur! Veuillez entrez un entier")
            continue
    else:
        break
final=notreListe(range(10,110))
print("Les valeurs de ma liste sont:",notreListe)
print("Les valeurs de ma liste sont:",final)
