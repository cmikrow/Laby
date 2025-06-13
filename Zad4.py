import networkx as nx
import matplotlib.pyplot as plt

# Tworzenie grafu nieskierowanego
G = nx.Graph()

# Dodawanie wierzchołków (można pominąć – doda się automatycznie z krawędziami)
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

# Dodawanie krawędzi (graf nieskierowany)
G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'A')
])

# Rysowanie grafu
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, edge_color='gray', font_size=12)

# Wyświetlanie
plt.title("Graf nieskierowany z 6 wierzchołkami")
plt.show()