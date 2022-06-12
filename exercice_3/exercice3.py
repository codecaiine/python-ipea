print("Entrez vos valeurs .. Puis taper sur la touche entrer pour terminer")
maListe = []
while True:
    valeur = input("Saisir une valeur: ")
    if valeur:
        try:
          maListe.append(int(valeur))
        except ValueError:
          print("Erreur! Veuillez entrez un entier")
          continue
    else:
        break
print("Vos valeurs sont : ", maListe)
length = len(maListe)
for i in range(length):
  print(i," : " , maListe[i])

somme_list = 0
for n in maListe:
    somme_list =+ n
print("La somme des element dans ma liste est:", somme_list)
