stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra",310.28,"Haut-parleurs", 27.00,"Télévision", 1000,"Cartes mères","souris","clavier",500,"barrettes de mémoire"]

print("Afficher la liste stock",stock)

chaines = []
nombres = []
for element in stock:
    if isinstance(element, str):
        chaines.append(element)
    elif isinstance(element, int) or isinstance(element, float):
        nombres.append(element)
print("La liste des chaines est: ",chaines)
print("La liste des nombres est: ",nombres)

nombre_str = len(chaines)
nombre_nbr = len(nombres)

print("Le nombre de chaines est: ",nombre_str)
print("Le nombre d'element dans la liste de nombres est :",nombre_nbr)

chaines.sort(key=str.lower)
print("La liste des chaines triées de a - z est :",chaines)

chaines.sort(key=str.lower, reverse=True)
print("La liste des chaines triées de z à a est :", chaines)

nombres.sort()