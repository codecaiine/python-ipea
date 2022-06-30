def supprimeDoublon(liste):
    secondListe = []
    for nombre in liste:
        if nombre in secondListe:
            pass 
        else:
            secondListe.append(nombre)
    return secondListe


print('Veuillez saisir un nombre....')
listedenombre = []
while True:
    entier = input('Veuillez saisir un nombre : ')
    if entier:
        try:
            listedenombre.append(int(entier))
        except ValueError:
            continue
    else:
        break
print(supprimeDoublon(listedenombre))