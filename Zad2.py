import queue
def sprawdz_nawiasy(wyrazenie):
    stos = queue.LifoQueue()
    for znak in wyrazenie:
        if znak == '(':
            stos.put(znak)
        elif znak == ')':
            if stos.empty():
                return False
            stos.get()
    return stos.empty()
wyrazenie = input("Podaj wyrażenie z nawiasami: ")
if sprawdz_nawiasy(wyrazenie):
    print("Nawiasy są poprawnie zagnieżdżone")
else:
    print("Nawiasy są niepoprawnie zagnieżdżone")
