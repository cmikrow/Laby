import time
def sekundnik():
    try:
        czas = int(input("Podaj czas w sekundach:"))
        if czas <= 0:
            print("Czas musi być liczbą dodatnią")
        else:
            while czas > 0:
                print(f"Pozostało: {czas} sekund do końca")
                time.sleep(1)
                czas -= 1
            print("KONIEC")
    except:
        print("Podaj poprawną liczbę całkowitą")
sekundnik()
