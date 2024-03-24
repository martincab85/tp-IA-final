import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()

# distancias en linea recta al nodo "B"
dlr = {"A": 77, "B": 00, "X": 55, "F": 12, "P": 10, "S": 22}

# Añadir nodos
nodos = ['A', 'X', 'P', 'F', 'S', 'B']
G.add_nodes_from(nodos)

# Añadir uniones con pesos
uniones = [
    ('A', 'X', {'weight': 1}), ('A', 'P', {'weight': 2}),
    ('A', 'F', {'weight': 1}),
    ('X', 'S', {'weight': 3}), ('X', 'B', {'weight': 2}),
    ('P', 'F', {'weight': 2}), ('P', 'S', {'weight': 2}),
    ('S', 'B', {'weight': 2}),
]
G.add_edges_from(uniones)

# Nodo inicial previamente seleccionado
nodo_inicial = 'A'  # Cambiar a cualquier nodo deseado
nodo_final = 'B'  # Cambiar a cualquier nodo deseado

if nodo_inicial not in nodos or nodo_final not in nodos:
    print(f"El nodo inicial {nodo_inicial} o nodo final {
          nodo_final} no se encuentran en la lista de nodos")

uniones_locales = []
# Iterar sobre las uniones
for union in uniones:
    if nodo_inicial == union[0] or nodo_inicial == union[1]:  # Verificar si el nodo inicial está en la unión
        uniones_locales.append(union)
        
print(uniones_locales)

# # Calcular el camino más corto
# shortest_path = nx.shortest_path(G, source=nodo_inicial, target=nodo_final)

# # Dibujar el grafo
# posiciones_nodos = nx.spring_layout(G)  # Posiciones de los nodos

# print(G.nodes())

# nx.draw(G, posiciones_nodos, with_labels=True, node_size=900,
#         node_color="skyblue", labels={node: node for node in G.nodes()})
# edge_labels_props = nx.draw_networkx_edge_labels(G, posiciones_nodos, edge_labels={
#                                                  (u, v): d['weight'] for u, v, d in G.edges(data=True)})

# print(shortest_path)

# if nodo_inicial:
#     nx.draw_networkx_nodes(G, posiciones_nodos, nodelist=[
#                            nodo_inicial], node_color='red', node_size=900)
# if nodo_final:
#     nx.draw_networkx_nodes(G, posiciones_nodos, nodelist=[
#                            nodo_final], node_color='green', node_size=900)

# # Dibujar los bordes del grafo sin el camino más corto
# nx.draw_networkx_edges(G, posiciones_nodos,
#                        edgelist=G.edges(), width=1.0, alpha=0.5)

# # Dibujar el camino más corto
# shortest_path_edges = [(shortest_path[i], shortest_path[i+1])
#                        for i in range(len(shortest_path)-1)]
# nx.draw_networkx_edges(G, posiciones_nodos,
#                        edgelist=shortest_path_edges, width=2, edge_color='red')

# # Dibujar las etiquetas de los bordes (pesos)
# edge_labels = nx.draw_networkx_edge_labels(G, posiciones_nodos, edge_labels={(u, v): d['weight']
#                                                                              for u, v, d in G.edges(data=True)})
# plt.show()
