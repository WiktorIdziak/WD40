import random
lista = []
for x in range (0, 100, 4):
    lista +=[x]
plik = open("dzielniki4.txt", "a+")
plik.writelines(str(lista))
plik.close()
