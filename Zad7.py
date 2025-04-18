import queue
q = queue.Queue()
menu = 0
while menu != 4:
    print("menu")
    print("1.Zarejestruj pacjenta")
    print("2.Wywołaj pacjenta od gabinetu")
    print("3.Podaż aktualną kolejke")
    print("4.Zakończ działanie programu")
    try:
        menu = int(input("(Wybierz działanie np'1')= "))
    except ValueError:
        print("Błąd: niepoprawny numer")
        continue
    if menu == 1:
        pacjent = input("Dodaj Pacjenta")
        q.put(pacjent)
        print(f"Dodano {pacjent} do kolejki")
    elif menu == 2:
        if q.empty():
            print("Brak pacjentów")
        else:
            print("Wywołano do gabinetu ",q.get())
    elif menu == 3:
        if q.empty():
            print("Pusta kolejka")
        else:
            print("Aktualna kolejak: ",list(q.queue))
    elif menu == 4:
        print("Zakończenie programu.")
    else:
        print("Niepoprawne dane")