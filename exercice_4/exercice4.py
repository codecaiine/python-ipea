print("Bienvenu dans notre programme")
notreListe=[]
nombre=0
for i in range(700, 1100):
    if (i%7==0) and (i%2!=0) and (i%5!=0):
        notreListe.append(i)
        nombre+=1
print(notreListe)
print("Le nombre trouvé es: ",nombre)