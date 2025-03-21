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
for i in lista:
    if i % 2 == 0:
        i_l_p += 1
print("Ilość liczb parzystych:", i_l_p)
