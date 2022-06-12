def supprimeDoublon(liste):
  initList = []
  for el in liste:
    if el not in initList:
      initList.append(el)
  return initList

print("Entrez les valeurs .. Tapez entrer pour terminer")
valeurListe = []
while True:
    valeur = input("Saisir une valeur: ")
    if valeur:
        valeurListe.append(int(valeur))
    else:
        break
print("Valeur entrées:", valeurListe)
print('La nouvelle liste est:', supprimeDoublon(valeurListe))    