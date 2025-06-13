graf = {
    'A': ['B'],
    'B': ['D'],
    'C': ['B'],
    'D': ['A','C','E'],
    'E': ['C']
}
wierzcholek = input("Wprowadź wierzchołek do sprawdzenia jego sąsiadów").upper()

if wierzcholek in graf:
    sasiedzi = graf[wierzcholek]
    print(f"Wiechołek: {wierzcholek}")
    print(f"Sąsiedzi: {sasiedzi}")
else:
    print("Niepoprawne dane")