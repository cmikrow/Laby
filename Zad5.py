def druga_najwieksza(lista):
    unikalne = list(set(lista))
    if len(unikalne) < 2:
        return "Ciąg musi zawierać co najmniej 2 różne liczby"
    unikalne.sort()
    return unikalne[-2]
lista = [1,2,3,3,4,4]
wynik = druga_najwieksza(lista)
print("Druga największa liczba:",wynik)