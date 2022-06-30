somme = 0
liste = []
dix_mille = 0
cinq_mille = 0
deux_mille = 0
mille = 0
cinq_cent = 0

i = 1
while i !=0:
    i = int(input("Veuillez saisir le prix"))
    liste.append(i)
    somme = somme + i
print("La somme totale est : ", somme)