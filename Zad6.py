import queue
q = queue.Queue()
n = int(input("Podaj n jako ilość kolejki: "))
for x in range(n):
    element = input("Podaj element: ")
    if element != "":
        q.put(element)
if q.empty() == True:
    print("Pusta kolejka")
else:
    print(list(q.queue))