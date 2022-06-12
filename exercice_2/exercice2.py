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
        try:
          valeurListe.append(int(valeur))
        except ValueError:
          print("Erreur! Veuillez entrez un entier")
          continue
    else:
        break
print("Valeur entrées:", valeurListe)
print('La nouvelle liste est:', supprimeDoublon(valeurListe))    