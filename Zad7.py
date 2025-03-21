def wynik(i):
    if i<5:
        print(i,"i<5")
        return 2
    elif i%2==0:
        print(i,"parzyste")
        return wynik(i-4)+wynik(i-2)+2
    else:
        print(i,"nieparzyste")
        return wynik(i-2)%9
for i in range(16):
    print(wynik(i))
    print("___koniec_funkcji___")