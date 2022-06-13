print("Entrez vos valeurs .. Puis taper sur la touche entrer pour terminer")
maListe=[]
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

somme_valeur=0
for n in maListe:
    somme_valeur+=n
print("La somme des element dans ma liste est:", somme_valeur)

multipleListe=[]
for m in maListe:
  multipleListe.append(m*3)
print("Ma nouvelle liste multiple de 3 est :", multipleListe)

max=0
for g in maListe:
  if g > max:
    max=g
print("Le plus grand est: ", max)

min=0
for p in maListe:
  if p < min:
    min=p
print("Le plus petit est: ", min)

pair=0
for p in maListe:
  if p %2==0:
    pair+=1
print("Le nombre de nombres pairs est: ", pair)

sommeImpairs=0
for p in maListe:
  if p %2!=0:
    sommeImpairs+=p
print("La somme des nombres impairs est: ", sommeImpairs)


