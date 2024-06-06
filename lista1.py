import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#o primeiro valor deixe como padrão e o último, coloque como o número de vértices + 1
G.add_nodes_from(range(1, 25))

#coloque as arestas do seu grafo
edges = [
  (1, 12),
  (2, 11), (2, 15),
  (3, 19), (3, 14),
  (4, 18), (4, 23),
  (5, 13), (5, 20),
  (6, 19), (6, 10),
  (7, 8), (7, 16), (7, 12),
  (8, 7), (8, 22), (8, 23),
  (9, 10), (9, 18), (9, 21),
  (10, 24), (10, 14), 
  (11, 15), (11, 14),
  (12, 22),
  (13, 20), (13, 24),
  (15, 20),
  (16, 17), (16, 21),
  (17, 20), (17, 19),
  (18, 23), (18, 21),
  (20, 22),
  (23, 24)
]

G.add_edges_from(edges)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='blue')
plt.show()