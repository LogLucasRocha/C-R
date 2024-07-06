import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#o primeiro valor deixe como padrão, já o último coloque como o número de vértices + 1
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
  (8, 22), (8, 23), 
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

def calcular_ordem(G):
  return G.number_of_nodes()

def calcular_tamanho(G):
  return G.number_of_edges()

def quantidade_componentes_conexos(G):
  return nx.number_connected_components(G)

def verificar_caminho_euleriano(G):
  if quantidade_componentes_conexos(G) > 1:
    return False

  for v in G.nodes:
    if G.degree(v) % 2 != 0:
      return False

  return True

def calcular_grau_medio(G):
  return 2 * calcular_tamanho(G) / calcular_ordem(G)

def calcular_diamentro(G):
  return nx.diameter(G)

def calcular_distancia_entre_dois_pontos(G, u, v):
  try:
    return nx.shortest_path_length(G, u, v)
  except:
    return ('infinito')

grau_medio = calcular_grau_medio(G)

print(f"A ordem do grafo é: {calcular_ordem(G)}")
print(f"O tamanho do grafo é: {calcular_tamanho(G)}")
print(f"A quantidade de componentes conexos é: {quantidade_componentes_conexos(G)}")
print(f"O grafo é euleriano: {verificar_caminho_euleriano(G)}")
print(f"O grau médio do grafo é: {grau_medio:.3f}")
print(f"O diâmetro do grafo é: {calcular_diamentro(G)}")
print(f"A distância entre os vértices 1 e 10 é: {calcular_distancia_entre_dois_pontos(G, 1, 10)}")
print(f"A distância entre os vértices 1 e 15 é: {calcular_distancia_entre_dois_pontos(G, 1, 15)}")
print(f"A distância entre os vértices 1 e 20 é: {calcular_distancia_entre_dois_pontos(G, 1, 20)}")

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='blue')
plt.show()
