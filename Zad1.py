Twoja_lista=[6,12,18,24,30,36]
Moja_lista=[1,17,3,5,3,4,86,90,2,21]
print(Twoja_lista)
print(Moja_lista)
print("__________")
Moja_lista.append(37)
print(Moja_lista)
Moja_lista.insert(8,1000)
print(Moja_lista)
Moja_lista.extend(Twoja_lista)
print(Moja_lista)
print("__________")
Moja_lista.remove(1)
print(Moja_lista)
Moja_lista.pop(1)
print(Moja_lista)
Moja_lista.clear()
print(Moja_lista)
print("__________")
Moja_lista=[1,17,3,5,3,4,86,90,2,21]
print(Moja_lista[7])
print(Moja_lista[3:10:2])
print("__________")
Moja_lista=[1,17,3,5,3,4,86,90,2,21]
Moja_lista.sort()
print(Moja_lista)
Moja_lista.reverse()
print(Moja_lista)
print("__________")
list=[1,17,3,5,3,4,86,90,2,21]
listx=[1,2,3]
listz=list+listx
print(len(list),max(list),min(list),sum(list),sorted(list),listz,list[:5],list[6:],list[2:6:1],list[::-3])