import heapq
q = heapq
kolejka = []
menu = 0
print("1. Dodaj zadanie z priorytetem")
print("2. Obsłuż zadanie o najwyższym priorytecie")
print("3. Pokaż kolejkę zadań")
print("4. Zakończ działanie programu")
while menu != "4":
    menu = input("Podaj numer opcji 1-4: ")
    if menu == "1":
        nazwa = input("Podaj nazwe zadanie: ")
        priorytet =  int(input("Podaj prorytet: "))
        q.heappush(kolejka,(priorytet,nazwa))
    elif menu == "2":
        if kolejka:
            priorytet,nazwa = q.heappop(kolejka)
            print(f"Zadanie z najwiekszym priorytetem to {priorytet}, {nazwa}")
        else:
            print("Kolejka zadań jest pusta")
    elif menu == "3":
        if kolejka:
            print("Aktualna kolejka zadań: ")
            for priorytet in sorted(kolejka):
                print(f"{nazwa} {priorytet}")
        else:
            print("Pusta kolejka")
    elif menu == "4":
        print("Koniec programu")
    else:
        print("Niepoprawne dane")