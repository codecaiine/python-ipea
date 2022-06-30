somme = 0
liste = []
dix_mille = 0
cinq_mille = 0
deux_mille = 0
mille = 0
cinq_cent = 0

i = 1
while i !=0:
    i = int(input("Veuillez saisir le prix de l article : "))
    liste.append(i)
    somme = somme + i
print("Le total des achats est : ", somme)
montant_remis = int(input('Saisir le montant remis par le client : '))
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
    mille +=1
    reste-= 1000
while reste > 500:
    cinq_cent +=1
    reste-= 500
print('Il y a {} billets de 10.000 FCFA'.format(dix_mille))
print('Il y a {} billets de 5.000 FCFA'.format(cinq_mille))
print('Il y a {} billets de 2.000 FCFA'.format(deux_mille))
print('Il y a {} billets de 1.000 FCFA'.format(mille))
print('Il y a {} billets de 500 FCFA'.format(cinq_cent))
print('La monnaie est : '.format(reste))