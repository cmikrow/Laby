import random
lista = []
l = range(1,50)
for i in l:
    lista.append(i)
print(lista)
losowanie = random.sample(lista,k=6)
print(losowanie)