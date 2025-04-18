import queue
print("Wprowadź 3 liczby")
q = queue.Queue()
for x in range(3):
    wpiszLiczbe = input(f"Wprowadź liczbe: {x+1}: ")
    q.put(wpiszLiczbe)
while not q.empty():
    print(q.get())