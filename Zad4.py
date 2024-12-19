import random
liczba_osob = int(input("Podaj liczbe osób w grupie"))
def rocznik_ucznia(osoby):
    rocznik = []
    for x in range(osoby):
        a = random.randint(1980,2005)
        rocznik.append(a)
    rocznik.sort()
    return rocznik
print(rocznik_ucznia(liczba_osob))
s = random.randint(1980,2005)
print("Twoja szczęśliwa liczba",s)

