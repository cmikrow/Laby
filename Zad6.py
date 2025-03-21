def znajdz_min_max(macierz):
    min_wartosc = macierz[0][0]
    max_wartosc = macierz[0][0]
    min_index = (0,0)
    max_index = (0,0)
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < min_wartosc:
                min_wartosc = macierz[i][j]
                min_index = (j,i)
            if macierz[i][j] > max_wartosc:
                max_wartosc = macierz[i][j]
                max_index = (j,i)
    macierz_wynik = [x[:] for x in macierz]
    macierz_wynik[min_index[1]][min_index[0]] = "MIN"
    macierz_wynik[max_index[1]][max_index[0]] = "MAX"
    print("Macierz po oznaczeniu MIN i MAX:")
    for x in macierz_wynik:
        print(x)
    print(f"MIN:{min_wartosc}, indeks:{min_index},(kolumna,wiersz)")
    print(f"MAX:{max_wartosc}, indeks:{max_index},(kolumna,wiersz)")
macierz =[
    [12,1,2],
    [4,5,7],
    [6,3,19],
    [2,3,5]
]
znajdz_min_max(macierz)