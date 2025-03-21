while True:
    n = int(input("Podaj liczbę n>0: "))
    if n > 0:
        break
lista = []
i_l_p = 0
for i in range(n):
    liczba = int(input(f"Podaj element {i + 1}: "))
    lista.append(liczba)
print("Wczytana lista:", lista)
c = int(input("Wprowadz liczbe c, by sprawdzić czy występuje w ciągu: "))
if c in lista:
    indeks = lista.index(c)
    print(f"Liczba c występuje w tym ciągu w indeksie {indeks}")
else:
    print("Liczba c nie występuje w tym ciągu")
