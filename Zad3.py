import queue
q = queue.LifoQueue()
while True:
    wprowadz = input("Podaj tekst(lub wpisz 'exit' aby wyjśc z programu): ")
    if wprowadz == "exit":
        print("Koniec programu")
        break
    elif wprowadz == "undo":
        if not q.empty():
            q.get()
    else:
        q.put(wprowadz)
    print("Tekst: ",' '.join(list(q.queue)))