import random
import math
p_od = int(input("Podaj liczbe do wylosowania z przdziału od"))
p_do = int(input("oraz do"))
krotka = ()
n = 10
i = 10
while i>0:
    p = random.randint(p_od,p_do)
    krotka += (p,)
    i -= 1
srednia = math.prod(krotka)
wynik = srednia**(1/n)
print(sorted(krotka))
print("Średnia geometryczna to {:.4f}".format(wynik))
