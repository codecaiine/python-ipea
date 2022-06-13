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

#Afficher la liste en colonne de manière à afficher l’index et sont contenu
length = len(maListe)
for i in range(length):
  print(i," : " , maListe[i])

#Additionner tous les éléments de la liste
somme_valeur=0
for n in maListe:
    somme_valeur+=n
print("La somme des element dans ma liste est:", somme_valeur)

#Créer une nouvelle liste qui sera le multiple (3) de tous les éléments de la liste
multipleListe=[]
for m in maListe:
  multipleListe.append(m*3)
print("Ma nouvelle liste multiple de 3 est :", multipleListe)

#Obtenir le plus grand nombre de la liste.
max=0
for g in maListe:
  if g > max:
    max=g
print("Le plus grand est: ", max)

#Obtenir le plus petit nombre de la liste.
min=0
for p in maListe:
  if p < min:
    min=p
print("Le plus petit est: ", min)

#Compter le nombre des nombres pairs présents dans la liste
pair=0
for p in maListe:
  if p %2==0:
    pair+=1
print("Le nombre de nombres pairs est: ", pair)

#Calculer la somme de tous les nombres pairs de la liste
sommePairs=0
for p in maListe:
  if p %2==0:
    sommePairs+=p
print("La somme des nombres impairs est: ", sommePairs)

#Compter le nombre des nombres impairs présents dans la liste
impair=0
for p in maListe:
  if p %2!=0:
    impair+=1
print("Le nombre de nombres pairs est: ", impair)

#Calculer la somme de tous les nombres impairs de la liste
sommeImpairs=0
for p in maListe:
  if p %2!=0:
    sommeImpairs+=p
print("La somme des nombres impairs est: ", sommeImpairs)


