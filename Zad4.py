import queue

wyrazenie = input("Wprowadz wyrażenie ONP: ")
def onp(wyrazenie):
    q = queue.LifoQueue()
    for znak in wyrazenie.split():
        if znak.isdigit():
            q.put(int(znak))
        elif znak in '+-*/^':
            b = q.get()  # Liczba z góry stosu
            a = q.get()
            if znak == '+':
                wynik = a + b
            elif znak == '-':
                wynik = a - b
            elif znak == '*':
                wynik = a * b
            elif znak == '/':
                wynik = a / b
            elif znak == '^':
                wynik = a ** b
            q.put(wynik)
        else:
            print(f"Niepoprawny znak {znak}")
    return q.get()
wynik = onp(wyrazenie)
print("Wynik: ",wynik)

