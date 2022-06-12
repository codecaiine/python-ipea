def supprimeDoublon(liste):
  initList = []
  for el in liste:
    if el not in initList:
      initList.append(el)
  return initList

print("Entrez vos valeurs .. Puis taper sur la touche entrer pour terminer")
valeurListe = []
while True:
    valeur = input("Saisir une valeur: ")
    if valeur:
        valeurListe.append(int(valeur))
    else:
        break
print("Valeur entrées:", valeurListe)
print('La nouvelle liste est:', supprimeDoublon(valeurListe))    