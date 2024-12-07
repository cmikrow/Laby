słownik = {
    "chleb":4.70,
    "masło":4.60,
    "mleko":2.50,
    "płatki śniadaniowe":9.90
}
print("Lista zakupów")
for artykul, kwota in słownik.items():
    print(f"{artykul}: {kwota} zł")
suma = sum(słownik.values())
print(f"Suma zakupów {suma} zł")