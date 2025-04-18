import queue
stos = queue.LifoQueue()
wprowadz = input("Wprowadź ciąg liczb")
for liczba in wprowadz:
    if liczba.isdigit():
        stos.put(liczba)
    else:
        print(f"Niepoprawną wartość:{liczba}")
print("Ciąg liczb w odwrotnej kolejności")
while not stos.empty():
    print(stos.get(),end="")
