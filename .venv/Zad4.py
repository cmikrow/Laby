x = int(input("Ilośc przyjaciół"))
n = int(input("Ilośc potraw"))
cena_potraw = 0
i = 0
while i < n:
    cena_dania = float(input(f"Podaj cene dania {i+1} "))
    cena_potraw += cena_dania
    i += 1
if n > 0:
    cena_zamowienia = cena_potraw/x
    print(f"{cena_zamowienia:.2f} średnia cena zamowienia na osobe")