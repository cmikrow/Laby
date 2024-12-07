def funkcja(a,*d):
    print("Zwykły parametr",a)
    for i in d:
        print(i)
wynik = funkcja(1,5,10,15)