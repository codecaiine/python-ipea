from locale import MON_2


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
montant_remis = int(input('Saisir le montant remis par le client'))
reste = montant_remis - somme
print("Le reste est : ", reste)

while reste > 10000:
    dix_mille +=1
    reste-= 10000
while reste > 5000:
    cinq_mille +=1
    reste-= 5000
while reste > 2000:
    deux_mille +=1
    reste-= 2000
while reste > 1000:
    reste-= 1000
while reste > 500:
    reste-= 500
print('Il y a {} billets de 10.000'.format(dix_mille))