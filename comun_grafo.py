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
    ('A', 'X'), ('A', 'P'), ('A', 'F'),
    ('X', 'S'), ('X', 'B'), ('P', 'F'),
    ('P', 'S'), ('S', 'B'),
]
G.add_edges_from(uniones)

# Nodo inicial previamente seleccionado
nodo_inicial = 'A'  # Cambiar a cualquier nodo deseado
nodo_final = 'B'  # Cambiar a cualquier nodo deseado

if nodo_inicial not in nodos or nodo_final not in nodos:
    print(f"El nodo inicial {nodo_inicial} o nodo final {
          nodo_final} no se encuentran en la lista de nodos")

nodos_actuales = {nodo_inicial: True}  # A
nodos_sucesores = []

def get_uniones(nodo):
    uniones_locales = []
    # Iterar sobre las uniones
    for union in uniones:
        # Verificar si el nodo inicial está en la unión
        if nodo == union[0]:
            uniones_locales.append(union[1])
        elif nodo == union[1]:
            uniones_locales.append(union[0])
    return uniones_locales

def get_actual_node():
    true_keys = [key for key, value in nodos_actuales.items() if value]
    true_key = true_keys[0]
    return true_key

def check_nodo_siguiente():
    nodo_actual = get_actual_node()
    nodo_siguiente = min(get_uniones(nodo_actual))  # F

    print(nodo_actual)
    print(nodo_siguiente)

    if nodo_siguiente != nodo_final:
        # agrego a la lista de nodos sucesores el expandido
        nodos_sucesores.append(nodo_siguiente)

        nodo_actual_value = dlr[nodo_actual]
        nodo_siguiente_value = dlr[nodo_siguiente]

        if nodo_siguiente_value <= nodo_actual_value:
            nodos_actuales[nodo_actual] = False
            nodos_actuales[nodo_siguiente] = True
        
        

        get_uniones(nodo_actual)
        print(nodos_actuales)
        print(nodos_sucesores)
    else:
        print('se termino el programa')
        print(nodos_actuales)
        print(nodos_sucesores)


check_nodo_siguiente()


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
