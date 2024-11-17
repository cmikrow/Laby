paliwo = 100
zuzycie_paliwa_na_s  = 10
czas = 0

while paliwo > 0:
    print(paliwo)
    paliwo -= zuzycie_paliwa_na_s
    czas += 1
print("Koniec lotu")